class PathfinderWorkshop {
    constructor() {
        this.init();
    }

    init() {
        let me = this;
        me.prepare_ajax();
    }

    prepare_ajax() {
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    let csrf_middlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
                    xhr.setRequestHeader('X-CSRFToken', csrf_middlewaretoken);
                }
            }
        });
    }

    revealUI() {
        let me = this;
        $('.header').removeClass('hidden');
        $('.menuzone').removeClass('hidden');
      //  $('.eventzone').removeClass('hidden');
      //  $('.userzone').removeClass('hidden');
      //  $('.wrapper').removeClass('hidden');
        $('.details').removeClass('hidden');
    }

    hideUI() {
        let me = this;
        $('.menuzone').addClass('hidden');
        $('.eventzone').addClass('hidden');
        $('.userzone').addClass('hidden');
        $('.wrapper').addClass('hidden');
        $('.details').addClass('hidden');
    }


    revealLog() {
        let me = this;
        // $('.menuzone').addClass('hidden');
        // $('.eventzone').addClass('hidden');
        // $('.userzone').addClass('hidden');
        // $('.wrapper').addClass('hidden');
        $('.adminzone').removeClass('hidden');
    }

    registerDisplay() {
        let me = this;
        $('.display').off().on('click', function (event) {
            let action = $(this).attr('action');
            let param = $(this).attr('param');
            let option = $(this).attr('option');
            // console.log(action+"|"+param+"|"+option)
            let key = $('#userinput').val();
            let url = 'ajax/display/' + action + '/';
            if (param != undefined) {
                let p = param.replaceAll('-', '_');
                if (option) {
                    url = 'ajax/display/' + action + '/' + p + '/' + option + '/';
                } else {
                    url = 'ajax/display/' + action + '/' + p + '/';
                }
            }
            // console.log(url);
            $.ajax({
                url: url,
                success: function (answer) {
                    if (action == 'session_details') {
                        $('.day_details').html(answer.data)
                    } else {
                        $('.wrapper').html(answer.data)
                    }
                    $('.menuzone').html(answer.menu)
                    me.rebootLinks();
                },
                error: function (answer) {
                    console.error(answer);
                    me.rebootLinks();
                },
            });
        });
    }

    registerOverlay() {
        let me = this;
        $('.modal_switch').off().on('click', function (event) {
            let action = $(this).attr('action');
            let param = $(this).attr('param');
            let option = $(this).attr('option');
            $('#callback').html("");
            let url = 'ajax/overlay/' + action + '/';
            if (param != undefined) {
                let p = param.replaceAll('-', '_');

                if (option) {
                    url = 'ajax/overlay/' + action + '/' + p + '/' + option + '/';
                } else {
                    url = 'ajax/overlay/' + action + '/' + p + '/';
                }
            }
            $.ajax({
                url: url,
                success: function (answer) {
                    let action_words = action.split("_")
                    if (action == 'close' || action_words[0] == 'confirm') {
                        $('#overlay').addClass('hidden');
                        $('#dialog').html("Nope");
                        if (option != undefined) {
                            $("#" + option).click();


                        }
                        $('.shuntable').removeClass('hidden')
                    } else {
                        $('#dialog').html(answer.data);
                        $('#overlay').removeClass('hidden');
                    }
                    me.rebootLinks();

                },
                error: function (answer) {
                    console.error(answer);
                    me.rebootLinks();
                },
            });
        });
    }

    registerToggle() {
        let me = this;
        $('.toggle').off().on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            let param = $(this).attr('param');
            if (param != undefined) {
                //$('.roster').addClass('hidden');
                $('#roster__'+param).toggleClass('hidden');
            }
            console.log('shoot');
        });
        console.log('Register Toggle!!');
    }

    registerAction() {
        let me = this;
        $('.action').off().on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            let action = $(this).attr('action');
            let param = $(this).attr('param');
            let option = $(this).attr('option');
            let respawn_id = '';
            // console.log(action + " " + param);
            if (action == 'model_edit') {
                if (param == 'game') {
                    respawn_id = 'ugr_' + option;
                } else if (param == 'proposition') {
                    respawn_id = 'upr_' + option;
                } else if (param == 'campaign') {
                    respawn_id = 'ucr_' + option;
                } else if (param == 'profile') {
                    respawn_id = 'uur_' + option;
                }
            }
            let form = $('#model_form');
            let formdata = form.serialize();

            let url = 'ajax/action/' + action + '/';
            if (param != undefined) {
                url += param + '/';
                if (option != undefined) {
                    url += option + '/';
                }
            }

            if (action == 'register_submit') {
                url = '/register_submit/';
                form = $('#register_form');
                formdata = form.serialize();
            }

            // console.log(formdata)

            $.ajax({
                url: url,
                type: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: formdata,
                dataType: 'json',
                success: function (answer) {
                    $('.shuntable').toggleClass('hidden')
                    $('.formblock').html(answer.form)
                    if (respawn_id) {
                        // console.log(respawn_id)
                        $("#" + respawn_id).html(answer.callback);

                    }
                    if (answer.form == "Okidoki!") {
                        $('#overlay').addClass('hidden');
                    }
                    if (action == 'register_submit') {
                        $(".invite_block").html(answer.data);
                    }
                    $('#reday').click();
                    $('#reday').css('border-color', "red");
                    // console.log("reday");


                    me.rebootLinks();
                },
                error: function (answer) {
                    console.error(answer);
                    $('.formblock').html(answer)
                },
            });
        });
    }


    registerPseudoLinks() {
        $('.pseudolink').off().on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            let action = $(this).attr('action');
            let param = $(this).attr('param');
            let url = '';
            if (param == 'direct') {
                url = '/' + action + '/';
                window.location = url;
            } else {
                url = 'ajax/' + action + '/';
            }
            $.ajax({
                url: url,
                type: 'POST',
                success: function (answer) {
                    window.location = '/';

                },
                error: function (answer) {
                    console.error(answer);
                },
            });
        });
    }

    rebootLinks() {
        let me = this;
        _.defer(function () {
            me.prepare_ajax()
            // me.registerDisplay();
            // me.registerOverlay();
            me.registerToggle();
            // me.registerAction();
            // me.registerPseudoLinks();
            console.log("Reboot links :)");
        });
    }

    perform() {
        console.log("Perform");
        let me = this;
        // me.loadAjax();
        me.rebootLinks();
    }

}




















