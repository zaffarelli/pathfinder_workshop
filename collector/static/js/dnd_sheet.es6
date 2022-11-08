class DnDSheet {
    constructor(data, parent, collector) {
        let me = this;
        me.parent = parent;
        me.co = collector;
        me.config = data;
        me.count = 0;

    }

    decorationText(x, y, d = 0, a = 'middle', f, s, b, c, w, t, v, o = 1) {
        let me = this;
        v.append('text')
            .attr("x", me.stepx * x)
            .attr("y", me.stepy * y)
            .attr("dy", d)
            .style("text-anchor", a)
            .style("font-family", f)
            .style("font-size", s + 'px')
            .style("fill", b)
            .style("stroke", c)
            .style("stroke-width", w + 'pt')
            .text(t)
            .attr('opacity', o);
    }

    sheet_type(str) {
        let res = "";
        switch (str) {
            case "garou":
                res = "Werewolf"
                break;
            case "fomori":
                res = "Fomori"
                break;
            case "kinfolk":
                res = "Kinfolk";
                break;
            case "changeling":
                res = "Changeling";
                break;
            case "ghoul":
                res = "Ghoul";
                break;
            case "wraith":
                res = "Wraith";
                break;
            case "mage":
                res = "Mage";
                break;
            case "kindred":
                res = "Vampire";
                break;
            default:
                res = "Mortal";
        }
        return res;
    }

    init() {
        let me = this;
        me.debug = false;
        me.page = 0;
        me.version = "1.0";
        me.date_release = "November 2022";
        me.blank = true;
        me.width = parseInt($(me.parent).css("width"), 10) * 0.75;
        me.height = me.width * 1.4;
        me.w = 1.25 * me.width;
        me.h = 1.25 * me.height;
        me.stepx = me.width / 24;
        me.stepy = me.height / 36;
        me.tiny_font_size = 0.9 * me.stepy / 5;
        me.small_font_size = 1.3 * me.stepy / 5;
        me.medium_font_size = 2 * me.stepy / 5;
        me.big_font_size = 3 * me.stepy / 5;
        me.fat_font_size = 8 * me.stepy / 5;
        me.margin = [0, 0, 0, 0];
        me.dot_radius = me.stepx / 8;
        me.stat_length = 150;
        me.stat_max = 5;
        me.shadow_fill = "#B0B0B0";
        me.shadow_stroke = "#A0A0A0";
        me.draw_stroke = '#CCC';
        me.draw_fill = '#222';
        me.user_stroke = '#66A';
        me.user_fill = '#224';
        me.user_font = 'Schoolbell';
        me.mono_font = 'Syne Mono';
        me.title_font = 'Khand';
        me.logo_font = 'UnifrakturMaguntia';
        me.base_font = 'Philosopher';
        me.x = d3.scaleLinear().domain([0, me.width]).range([0, me.width]);
        me.y = d3.scaleLinear().domain([0, me.height]).range([0, me.height]);
        me.pre_title = me.config['pre_title'];
        me.scenario = me.config['scenario'];
        me.post_title = me.config['post_title'];
        me.health_levels = ['Bruised/X', 'Hurt/-1', 'Injured/-1', 'Wounded/-2', 'Mauled/-2', 'Crippled/-5', 'Incapacitated/X'];
    }


    midline(y, startx = 2, stopx = 22) {
        let me = this;
        me.back.append('line')
            .attr('x1', me.stepx * startx)
            .attr('x2', me.stepx * stopx)
            .attr('y1', me.stepy * y)
            .attr('y2', me.stepy * y)
            .style('fill', 'transparent')
            .style('stroke', me.draw_fill)
            .style('stroke-width', '3pt')
            .style('stroke-linecap', 'round')
        // .attr('marker-end', "url(#arrowhead)")
        // .attr('marker-start', "url(#arrowhead)")
        ;
    }

    crossline(x, starty = 2, stopy = 35) {
        let me = this;
        me.back.append('line')
            .attr('x1', me.stepx * x)
            .attr('x2', me.stepx * x)
            .attr('y1', me.stepy * starty)
            .attr('y2', me.stepy * stopy)
            .style('fill', 'transparent')
            .style('stroke', me.draw_fill)
            .style('stroke-width', '3pt')
            .style('stroke-linecap', 'round')
        // .attr('marker-end', "url(#arrowhead)")
        // .attr('marker-start', "url(#arrowhead)")
        ;
    }


    drawWatermark() {
        let me = this;
        d3.select(me.parent).selectAll("svg").remove();
        // me.svg = d3.select(me.parent).append("svg")
        //     .attr("id", me.data['rid'])
        //     .attr("viewBox", "0 0 " + me.w + " " + me.h)
        //     .attr("width", me.width)
        //     .attr("height", me.height)
        //     .append("svg:g")
        //     .attr("transform", "translate(0,0)")
        // .call(d3.behavior.zoom().x(me.x).y(me.y).scaleExtent([2, 8]).on("zoom", function(e){
        //     })
        // )
        // ;
        // d3.select(me.parent).selectAll("svg").remove();
        me.vis = d3.select(me.parent).append("svg")
            .attr("id", me.data['rid'])
            .attr("class", "pathfinder_sheet")
            .attr("viewBox", "0 0 " + me.w + " " + me.h)
            .attr("width", me.w)
            .attr("height", me.h);
        me.svg = me.vis.append("g")
            .attr("class", "all")
            .attr("transform", "translate(0,0)");
        me.back = me.svg
            .append("g")
            .attr("class", "page")
            .attr("transform", "translate(" + 0 * me.stepx + "," + 0 * me.stepy + ")");
        me.defs = me.svg.append('defs');
        me.defs.append('marker')
            .attr('id', 'arrowhead')
            .attr('viewBox', '-0 -5 10 10')
            .attr('refX', 0)
            .attr('refY', 0)
            .attr('orient', 'auto-start-reverse')
            .attr('markerWidth', 9)
            .attr('markerHeight', 9)
            .attr('preserveAspectRatio', 'xMidYMid meet')
            .attr('xoverflow', 'visible')

            .append('svg:path')
            .attr('d', 'M 1,-1 l 3,1 -3,1 -1,-1 1,-1 M 5,-1 l  3,1 -3,1 -1,-1 1,-1   Z')
            .style('fill', me.draw_fill)
            .style('stroke', me.draw_stroke)
            .style('stroke-width', '0pt');
        me.back.append('rect')
            .attr('x', 0)
            .attr('y', 0)
            .attr('width', me.width)
            .attr('height', me.height)
            .style('fill', 'white')
            .style('stroke', me.draw_stroke)
            .style('stroke-width', '0')
            .attr('opacity', 1.0);
        // Grid
        if (me.debug) {
            let verticals = me.back.append('g')
                .attr('class', 'verticals')
                .selectAll("g")
                .data(d3.range(0, 24, 1));
            verticals.enter()
                .append('line')
                .attr('x1', function (d) {
                    return d * me.stepx
                })
                .attr('y1', 0)
                .attr('x2', function (d) {
                    return d * me.stepx
                })
                .attr('y2', 36 * me.stepy)
                .style('fill', 'transparent')
                .style('stroke', '#CCC')
                .style('stroke-width', '0.25pt');
            let horizontals = me.back.append('g')
                .attr('class', 'horizontals')
                .selectAll("g")
                .data(d3.range(0, 36, 1));
            horizontals.enter()
                .append('line')
                .attr('x1', 0)
                .attr('x2', 24 * me.stepx)
                .attr('y1', function (d) {
                    return d * me.stepy
                })
                .attr('y2', function (d) {
                    return d * me.stepy
                })
                .style('fill', 'transparent')
                .style('stroke', '#CCC')
                .style('stroke-width', '0.25pt');
        }

        // Sheet content
        me.character = me.back.append('g')
            .attr('class', 'xover_sheet');

        me.drawPages();
    }

    stdField(label, value, ox, oy, size = 3) {
        let me = this;
        let item = me.daddy.append('g')
            .attr('class', 'std_field_grp');
        item.append('line')
            .attr('x1', ox * me.stepx)
            .attr('y1', oy * me.stepy)
            .attr('x2', (ox + size) * me.stepx)
            .attr('y2', oy * me.stepy)
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')

        ;
        item.append('text')
            .attr("x", ox * me.stepx)
            .attr("y", oy * me.stepy)
            .attr("dy", "12pt")
            .style("text-anchor", 'start')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'px')
            .style("fill", me.draw_fill)
            .style("stroke", me.draw_stroke)
            .style("stroke-width", '0.5pt')
            .text(label);
        if (me.blank == false) {
            item.append('text')
                .attr("x", ox * me.stepx)
                .attr("y", oy * me.stepy)
                .attr("dy", "-6pt")
                .style("text-anchor", 'start')
                .style("font-family", me.user_font)
                .style("font-size", me.small_font_size + 'pt')
                .style("fill", me.user_fill)
                .style("stroke", me.user_stroke)
                .style("stroke-width", '0.5pt')
                .text(value);
        }
    }

    smallField(value, ox, oy, size = 3, wob = false) {
        let me = this;
        let item = me.daddy.append('g')
            .attr('class', 'std_field_grp');
        if (wob) {
            item.append('rect')
                .attr('x', ox * me.stepx)
                .attr('y', (oy-0.5) * me.stepy)
                .attr('width', size * me.stepx)
                .attr('height', 0.5*me.stepy)
                .style("fill", me.draw_fill)
                .style("stroke", me.shadow_stroke)
                .style("stroke-width", '1.0pt')
            ;
            item.append('text')
                .attr("x", (ox + size/2)  * me.stepx)
                .attr("y", (oy) * me.stepy)
                .attr("dy", -me.small_font_size/2)
                .style("text-anchor", 'middle')
                .style("font-family", me.title_font)
                .style("font-size", me.small_font_size + 'px')
                .style("fill", "#F0F0F0")
                .style("stroke", "#C0C0C0")
                .style("stroke-width", '0.5pt')
                .text(value);
        } else {
            item.append('line')
                .attr('x1', ox * me.stepx)
                .attr('y1', oy * me.stepy)
                .attr('x2', (ox + size) * me.stepx)
                .attr('y2', (oy) * me.stepy)
                .style("fill", me.draw_fill)
                .style("stroke", me.shadow_stroke)
                .style("stroke-width", '1.0pt')

            ;
            if (me.blank == false) {
                item.append('text')
                    .attr("x", ox * me.stepx)
                    .attr("y", oy * me.stepy)
                    .attr("dy", "-6pt")
                    .style("text-anchor", 'start')
                    .style("font-family", me.user_font)
                    .style("font-size", me.tiny_font_size + 'pt')
                    .style("fill", me.user_fill)
                    .style("stroke", me.user_stroke)
                    .style("stroke-width", '0.5pt')
                    .text(value);
            }
        }


    }


    skillField(ox, oy, rank, no_header=1) {
        let me = this;
        let size = 4;
        let item = me.daddy.append('g')
            .attr('class', 'skill_text_grp');
        let r = $.parseJSON(rank);

        item.append('rect')
            .attr('x', function (d, i) {
                return ox;
            })
            .attr('y', function (d, i) {
                return oy - 0.1 * me.stepy;
            })
            .attr('width', function (d, i) {
                return 0.2 * me.stepx;
            })
            .attr('height', function (d, i) {
                return 0.2 * me.stepy;
            })
            .style("fill", function (d, i) {
                if (me.blank == false) {
                    if (r.is_class_skill) {
                        return me.draw_fill;
                    }
                }
                return "transparent";
            })
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')

        ;

        item.append('text')
            .attr("x", ox + 0.5 * me.stepx)
            .attr("y", oy)
            .attr("dy", "6pt")
            .style("text-anchor", 'start')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'pt')
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .text(function (d) {
                let s = r.skill_name;
                if (r.is_trained_only) {
                    s += " *";
                }
                if (r.acp_applies) {
                    s += " ¤";
                }
                if (r.wildcard) {
                    s += " (" + r.wildcard + ")"
                }
                return s
            });

        item.append('rect')
            .attr("x", ox + 4.2 * me.stepx)
            .attr("y", oy - 0.3 * me.stepy)
            .attr('width', function (d, i) {
                return 0.6 * me.stepx;
            })
            .attr('height', function (d, i) {
                return 0.6 * me.stepy;
            })
            .style("fill", function (d, i) {
                return "transparent";
            })
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '2.0pt')

        ;

        if (no_header == 0){
            item.append('text')
            .attr("x", ox + 4.5 * me.stepx)
            .attr("y", oy - 0.6 * me.stepy)
            .attr("dy", "4pt")
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'pt')
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .text("Rnk");

            item.append('text')
            .attr("x", ox + 6.8 * me.stepx)
            .attr("y", oy - 0.6 * me.stepy)
            .attr("dy", "4pt")
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'pt')
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .text("CC");

            item.append('text')
            .attr("x", ox + 7.5 * me.stepx)
            .attr("y", oy - 0.6 * me.stepy)
            .attr("dy", "4pt")
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'pt')
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .text("ACP");

            item.append('text')
            .attr("x", ox + 8.2 * me.stepx)
            .attr("y", oy - 0.6 * me.stepy)
            .attr("dy", "4pt")
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'pt')
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .text("MOD");

            item.append('text')
            .attr("x", ox + 9.1 * me.stepx)
            .attr("y", oy - 0.6 * me.stepy)
            .attr("dy", "4pt")
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'pt')
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .text("VAL");
        }



        item.append('text')
            .attr("x", ox + 5.3 * me.stepx)
            .attr("y", oy)
            .attr("dy", "6pt")
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'pt')
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .text(r.ability);




        item.append('rect')
            .attr("x", ox + 5.6 * me.stepx)
            .attr("y", oy - 0.3 * me.stepy)
            .attr('width', function (d, i) {
                return 0.6 * me.stepx;
            })
            .attr('height', function (d, i) {
                return 0.6 * me.stepy;
            })
            .style("fill", function (d, i) {
                return "transparent";
            })
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')
        ;



        item.append('rect')
            .attr("x", ox + 6.5 * me.stepx)
            .attr("y", oy - 0.3 * me.stepy)
            .attr('width', function (d, i) {
                return 0.6 * me.stepx;
            })
            .attr('height', function (d, i) {
                return 0.6 * me.stepy;
            })
            .style("fill", function (d, i) {
                return "transparent";
            })
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')

        ;



        item.append('rect')
            .attr("x", ox + 7.2 * me.stepx)
            .attr("y", oy - 0.3 * me.stepy)
            .attr('width', function (d, i) {
                return 0.6 * me.stepx;
            })
            .attr('height', function (d, i) {
                return 0.6 * me.stepy;
            })
            .style("fill", function (d, i) {
                return "transparent";
            })
            .style("stroke", me.shadow_stroke)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')

        ;



        item.append('rect')
            .attr("x", ox + 7.9 * me.stepx)
            .attr("y", oy - 0.3 * me.stepy)
            .attr('width', function (d, i) {
                return 0.6 * me.stepx;
            })
            .attr('height', function (d, i) {
                return 0.6 * me.stepy;
            })
            .style("fill", function (d, i) {
                return "transparent";
            })
            .style("stroke", me.shadow_stroke)
            .style("stroke-dasharray", "2 2")
            .style("stroke-width", '1.0pt')

        ;

        item.append('rect')
            .attr("x", ox + 8.8 * me.stepx)
            .attr("y", oy - 0.3 * me.stepy)
            .attr('width', function (d, i) {
                return 0.6 * me.stepx;
            })
            .attr('height', function (d, i) {
                return 0.6 * me.stepy;
            })
            .style("fill", function (d, i) {
                return "transparent";
            })
            .style("stroke", "#000")
            .style("stroke-width", '1.0pt')

        ;

        if (me.blank == false) {
            item.append('text')
                .attr("x", ox + 6.5 * me.stepx)
                .attr("y", oy)
                .attr("dy", "6pt")
                .style("text-anchor", 'middle')
                .style("font-family", me.user_font)
                .style("font-size", me.small_font_size + 'pt')
                .style("fill", me.user_fill)
                .style("stroke", me.user_stroke)
                .style("stroke-width", '0.5pt')
                .text(r.ab_mod);


            item.append('text')
                .attr("x", ox + 7.0 * me.stepx)
                .attr("y", oy)
                .attr("dy", "6pt")
                .style("text-anchor", 'middle')
                .style("font-family", me.user_font)
                .style("font-size", me.small_font_size + 'pt')
                .style("fill", me.user_fill)
                .style("stroke", me.user_stroke)
                .style("stroke-width", '0.5pt')
                .text(function (d) {
                    if (r.rank == 0) {
                        return "-"
                    }
                    return r.rank
                });
            item.append('text')
                .attr("x", ox + 7.6 * me.stepx)
                .attr("y", oy)
                .attr("dy", "6pt")
                .style("text-anchor", 'middle')
                .style("font-family", me.user_font)
                .style("font-size", me.small_font_size + 'pt')
                .style("fill", me.user_fill)
                .style("stroke", me.user_stroke)
                .style("stroke-width", '0.5pt')
                .text(function (d) {
                    if (r.is_class_skill) {
                        if (r.rank > 0) {
                            return "+3"
                        }
                    }
                    return "-"
                });


            item.append('text')
                .attr("x", ox + 4.5 * me.stepx)
                .attr("y", oy)
                .attr("dy", "6pt")
                .style("text-anchor", 'middle')
                .style("font-family", me.user_font)
                .style("font-size", me.small_font_size + 'pt')
                .style("fill", me.user_fill)
                .style("stroke", me.user_stroke)
                .style("stroke-width", '0.5pt')
                .text(function (d) {
                    if (r.is_trained_only) {
                        if (r.rank == 0) {
                            return "-"
                        }
                    }
                    return r.total
                });
        }
    }


    simpleText(label, ox, oy, size = 3) {
        let me = this;
        let item = me.daddy.append('g')
            .attr('class', 'simple_text_grp');

        item.append('text')
            .attr("x", ox + size * me.stepx / 2)
            .attr("y", oy)
            .attr("dy", "6pt")
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.tiny_font_size + 'pt')
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .text(label);
    }


    attField(label, label_full, value, value_mod, ox, oy, width = 3, height = 0.5, att = false) {
        let me = this;
        let item = me.daddy.append('g')
            .attr('class', 'attr_grp');
        item.append('rect')
            .attr('x', function (d, i) {
                return ox;
            })
            .attr('y', function (d, i) {
                return oy;
            })
            .attr('width', function (d, i) {
                return width * me.stepx;
            })
            .attr('height', function (d, i) {
                return height * me.stepy;
            })
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')

        ;
        item.append('rect')
            .attr('x', function (d, i) {
                return ox + (width + 0.1) * me.stepx;
            })
            .attr('y', function (d, i) {
                return oy;
            })
            .attr('width', function (d, i) {
                return me.stepx * 0.8;
            })
            .attr('height', function (d, i) {
                return height * me.stepy;
            })
            .style("fill", "transparent")
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt');

        if (att) {
            item.append('rect')
                .attr('x', function (d, i) {
                    return ox + (width + 1.1) * me.stepx;
                })
                .attr('y', function (d, i) {
                    return oy;
                })
                .attr('width', function (d, i) {
                    return me.stepx * 0.8;
                })
                .attr('height', function (d, i) {
                    return height * me.stepy;
                })
                .style("fill", "transparent")
                .style("stroke", me.shadow_stroke)
                .style("stroke-width", '1.0pt');

            item.append('rect')
                .attr('x', function (d, i) {
                    return ox + (width + 2.1) * me.stepx;
                })
                .attr('y', function (d, i) {
                    return oy;
                })
                .attr('width', function (d, i) {
                    return me.stepx * 0.8;
                })
                .attr('height', function (d, i) {
                    return height * me.stepy;
                })
                .style("fill", "transparent")
                .style("stroke", me.shadow_stroke)
                .style("stroke-width", '1.0pt');

            item.append('rect')
                .attr('x', function (d, i) {
                    return ox + (width + 3.1) * me.stepx;
                })
                .attr('y', function (d, i) {
                    return oy;
                })
                .attr('width', function (d, i) {
                    return me.stepx * 0.8;
                })
                .attr('height', function (d, i) {
                    return height * me.stepy;
                })
                .style("fill", "transparent")
                .style("stroke", me.shadow_stroke)
                .style("stroke-width", '1.0pt');
        }

        item.append('text')
            .attr("x", ox + width * me.stepx / 2)
            .attr("y", oy + height * me.stepy / 2)
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.medium_font_size + 'px')
            .style("fill", "#F0F0F0")
            .style("stroke", "#F0F0F0")
            .style("stroke-width", '0.5pt')
            .text(label);
        item.append('text')
            .attr("x", ox + width * me.stepx / 2)
            .attr("y", oy + height * me.stepy / 2)
            .attr("dy", "12pt")
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'px')
            .style("fill", "#F0F0F0")
            .style("stroke", "#C0C0C0")
            .style("stroke-width", '0.5pt')
            .text(label_full);
        if (me.blank == false) {
            item.append('text')
                .attr("x", ox + me.stepx * width + me.stepx * 0.5)
                .attr("y", oy + me.stepx * 0.15)
                .attr("dy", "18pt")
                .style("text-anchor", 'middle')
                .style("font-family", me.user_font)
                .style("font-size", me.medium_font_size + 'pt')
                .style("fill", me.user_fill)
                .style("stroke", me.user_stroke)
                .style("stroke-width", '0.5pt')
                .text(value);
            if (att) {
                item.append('text')
                    .attr("x", ox + me.stepx * width + me.stepx * 1.5)
                    .attr("y", oy + me.stepx * 0.15)
                    .attr("dy", "18pt")
                    .style("text-anchor", 'middle')
                    .style("font-family", me.user_font)
                    .style("font-size", me.medium_font_size + 'pt')
                    .style("fill", me.user_fill)
                    .style("stroke", me.user_stroke)
                    .style("stroke-width", '0.5pt')
                    .text(value_mod);
            }
        }
    }

    boxField(label_full, data_field, ox, oy, width = 1, height = 0.8, wob = false, label = "", preserve = false, direct_value=false) {
        let me = this;
        let item = me.daddy.append('g')
            .attr('class', 'attr_grp');
        let th = 0.1;
        if (wob == true) {
            th = 0;
        }
        item.append('rect')
            .attr('x', function (d, i) {
                return (ox + th) * me.stepx;
            })
            .attr('y', function (d, i) {
                return oy * me.stepy;
            })
            .attr('width', function (d, i) {
                return (width - 2 * th) * me.stepx;
            })
            .attr('height', function (d, i) {
                return height * me.stepy;
            })
            .style("fill", function (d) {
                if (wob) {
                    return me.draw_fill;
                }
                return "transparent";
            })
            .style("stroke", function (d) {
                return me.shadow_stroke;
            })
            .style("stroke-width", '1.0pt')
        ;
        if (wob) {
            item.append('text')
                .attr('x', function (d, i) {
                    return (ox + width * 0.5) * me.stepx;
                })
                .attr('y', (oy + 0.4) * me.stepy)
                .style("text-anchor", 'middle')
                .style("font-family", me.title_font)
                .style("font-size", me.medium_font_size + 'px')
                .style("fill", "#F0F0F0")
                .style("stroke", "#C0C0C0")
                .style("stroke-width", '0.5pt')
                .text(label_full)
            ;
            item.append('text')
                .attr('x', function (d, i) {
                    return (ox + width * 0.5) * me.stepx;
                })
                .attr('y', (oy + 0.65) * me.stepy)
                .style("text-anchor", 'middle')
                .style("font-family", me.title_font)
                .style("font-size", me.tiny_font_size + 'pt')
                .style("fill", "#F0F0F0")
                .style("stroke", "#C0C0C0")
                .style("stroke-width", '0.5pt')
                .text(label)
            ;
        } else {
            let words = []
            if (preserve) {
                words = [label_full];
            }else{
                words = label_full.split(" ");
            }
            item.append('text')
                .attr('x', function (d, i) {
                    return (ox + width * 0.5) * me.stepx;
                })
                .attr('y', function (d) {
                    if (preserve) {
                        return (oy + 0.3) * me.stepy
                    }
                    if (words.length == 1) {
                        return (oy - 0.1) * me.stepy
                    }
                    return (oy - 0.3) * me.stepy
                })
                .style("text-anchor", 'middle')
                .style("font-family", me.title_font)
                .style("font-size", me.tiny_font_size + 'pt')
                .style("fill", me.draw_fill)
                .style("stroke", me.draw_stroke)
                .style("stroke-width", '0.5pt')
                .text(words[0])
            ;
            if (words.length > 1) {
                item.append('text')
                    .attr('x', function (d, i) {
                        return (ox + width * 0.5) * me.stepx;
                    })
                    .attr('y', (oy - 0.05) * me.stepy)
                    .style("text-anchor", 'middle')
                    .style("font-family", me.title_font)
                    .style("font-size", me.tiny_font_size + 'pt')
                    .style("fill", me.draw_fill)
                    .style("stroke", me.draw_stroke)
                    .style("stroke-width", '0.5pt')
                    .text(words[1])
                ;
            }

            if (me.blank == false) {
                item.append('text')
                    .attr('x', function (d, i) {
                        return (ox + width * 0.5) * me.stepx;
                    })
                    .attr('y', (oy + 0.5) * me.stepy)
                    .attr('width', me.stepx * 0.8)
                    .attr('height', (height) * me.stepy)
                    .style("text-anchor", 'middle')
                    .style("font-family", me.user_font)
                    .style("font-size", me.medium_font_size + 'px')
                    .style("fill", me.user_fill)
                    .style("stroke", me.user_stroke)
                    .style("stroke-width", '1.0pt')
                    .text(function (d) {
                        if (direct_value == true){
                            return data_field;
                        }
                        if (data_field == 0) {
                            return ""
                        }
                        return me.data[data_field];
                    })
                ;
            }
        }
    }


    acField(label, label_full, value, value_mod, ox, oy, width = 3, height = 0.5, type = "ac") {
        let me = this;
        let item = me.daddy.append('g')
            .attr('class', 'attr_grp');
        // Base box
        item.append('rect')
            .attr('x', function (d, i) {
                return ox;
            })
            .attr('y', function (d, i) {
                return oy;
            })
            .attr('width', function (d, i) {
                return width * me.stepx;
            })
            .attr('height', function (d, i) {
                return height * me.stepy;
            })
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')

        ;
        let squares = [{
            "num": 0,
            "thickness": 3,
            "types": ["ac", "touch", "ff"]
        }, {
            "num": 2,
            "types": ["ac", "ff"],
            "thickness": 1,
            "value": "AC_armor_bonus"
        }, {
            "num": 3,
            "types": ["ac", "ff"],
            "thickness": 1,
            "value": "AC_shield_bonus"
        }, {
            "num": 4,
            "types": ["ac", "touch"],
            "thickness": 1,
            "value": "DEX_mod"
        }, {
            "num": 5,
            "types": ["ac", "touch", "ff"],
            "thickness": 1,
            "value": "AC_size_modifier"
        }, {
            "num": 6,
            "types": ["ac", "ff"],
            "thickness": 1,
            "value": "AC_natural_armor"
        }, {
            "num": 7,
            "types": ["ac", "touch"],
            "thickness": 1,
            "value": "AC_deflection_bonus"
        }, {
            "num": 8,
            "types": ["ac", "touch", "ff"],
            "thickness": 1,
            "value": "AC_temporary_modifier"
        }];
        _.forEach(squares, function (v, k) {
            if (v['types'].includes(type)) {
                item.append('rect')
                    .attr('x', function (d, i) {
                        return ox + (width + v['num'] + 0.1) * me.stepx;
                    })
                    .attr('y', oy)
                    .attr('width', me.stepx * 0.8)
                    .attr('height', height * me.stepy)
                    .style("fill", "transparent")
                    .style("stroke", me.shadow_stroke)
                    .style("stroke-width", v['thickness'] + 'pt')
                ;
                if ((me.blank == false) & (v['num'] > 0)) {
                    item.append('text')
                        .attr('x', function (d, i) {
                            return ox + (width + 0.5 + v['num']) * me.stepx;
                        })
                        .attr('y', oy + 0.5 * me.stepy)
                        .attr('width', me.stepx * 0.8)
                        .attr('height', (height) * me.stepy)
                        .style("text-anchor", 'middle')
                        .style("font-family", me.user_font)
                        .style("font-size", me.medium_font_size + 'px')
                        .style("fill", me.user_fill)
                        .style("stroke", me.user_stroke)
                        .style("stroke-width", '1.0pt')
                        .text(me.data[v['value']]);
                }
            }
        })


        item.append('text')
            .attr("x", ox + width * me.stepx / 2)
            .attr("y", oy + height * me.stepy / 2)
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.medium_font_size + 'px')
            .style("fill", "#F0F0F0")
            .style("stroke", "#F0F0F0")
            .style("stroke-width", '0.5pt')
            .text(label);

        item
            .append('text')
            .attr("x", ox + width * me.stepx / 2)
            .attr("y", oy + height * me.stepy * 1.7 / 2)
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'px')
            .style("fill", "#F0F0F0").style("stroke", "#C0C0C0")
            .style(
                "stroke-width",
                '0.5pt'
            )
            .text(label_full);


        item.append('text').attr("x", ox + (width + 0.5) * me.stepx)
            .attr("y", oy + height * me.stepy * 1.5 / 2)
            .style("text-anchor", 'middle')
            .style("font-family", me.user_font)
            .style("font-size", me.big_font_size + 'px')
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
            .style("stroke-width", '0.5pt')
            .text(value);
    }

    floatingText(ox, oy, txt) {
        let me = this;
        let item = me.daddy.append('g')
            .attr('class', 'attr_grp');
        item.append('text')
            .attr("x", ox * me.stepx)
            .attr("y", oy * me.stepy)
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.medium_font_size + 'px')
            .style("fill", me.draw_fill)
            .style("stroke", me.draw_stroke)
            .style("stroke-width", '0.5pt')
            .text(txt);
    }


    saveField(label, label_full, value, value_mod, ox, oy, width = 3, height = 0.5, type = "ac") {
        let me = this;
        let item = me.daddy.append('g')
            .attr('class', 'attr_grp');
        // Base box
        item.append('rect')
            .attr('x', function (d, i) {
                return ox;
            })
            .attr('y', function (d, i) {
                return oy;
            })
            .attr('width', function (d, i) {
                return width * me.stepx;
            })
            .attr('height', function (d, i) {
                return height * me.stepy;
            })
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')

        ;
        let squares = [{
            "num": 0,
            "thickness": 3

        }, {
            "num": 1,
            "thickness": 1,
            "value": "AC_armor_bonus"
        }, {
            "num": 2,
            "thickness": 1,
            "value": "AC_shield_bonus"
        }, {
            "num": 3,
            "thickness": 1,
            "value": "DEX_mod"
        }, {
            "num": 4,
            "thickness": 1,
            "value": "AC_size_modifier"
        }, {
            "num": 5,
            "thickness": 1,
            "value": "AC_natural_armor"
        }];
        _.forEach(squares, function (v, k) {

            item.append('rect')
                .attr('x', function (d, i) {
                    return ox + (width + v['num'] + 0.1) * me.stepx;
                })
                .attr('y', oy)
                .attr('width', me.stepx * 0.8)
                .attr('height', height * me.stepy)
                .style("fill", "transparent")
                .style("stroke", me.shadow_stroke)
                .style("stroke-width", v['thickness'] + 'pt')
            if ((me.blank == false) & (v['num'] > 0)) {
                item.append('text')
                    .attr('x', function (d, i) {
                        return ox + (width + 0.5 + v['num']) * me.stepx;
                    })
                    .attr('y', oy + 0.5 * me.stepy)
                    .attr('width', me.stepx * 0.8)
                    .attr('height', (height) * me.stepy)
                    .style("text-anchor", 'middle')
                    .style("font-family", me.user_font)
                    .style("font-size", me.medium_font_size + 'px')
                    .style("fill", me.user_fill)
                    .style("stroke", me.user_stroke)
                    .style("stroke-width", '1.0pt')
                    .text(me.data[v['value']]);
            }

        })

        item.append('text')
            .attr("x", ox + width * me.stepx / 2)
            .attr("y", oy + height * me.stepy / 2)
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.medium_font_size + 'px')
            .style("fill", "#F0F0F0")
            .style("stroke", "#F0F0F0")
            .style("stroke-width", '0.5pt')
            .text(label);

        item.append('text')
            .attr("x", ox + width * me.stepx / 2)
            .attr("y", oy + height * me.stepy * 1.7 / 2)
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.small_font_size + 'px')
            .style("fill", "#F0F0F0").style("stroke", "#C0C0C0")
            .style(
                "stroke-width",
                '0.5pt'
            )
            .text(label_full);


        item.append('text').attr("x", ox + (width + 0.5) * me.stepx)
            .attr("y", oy + height * me.stepy * 1.5 / 2)
            .style("text-anchor", 'middle')
            .style("font-family", me.user_font)
            .style("font-size", me.big_font_size + 'px')
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
            .style("stroke-width", '0.5pt')
            .text(value);
    }


    reinHagenStat(name, value, ox, oy, type, statcode, source, power = false) {
        let me = this;
        let item = source.append('g')
            .attr('class', type);
        item.append('rect')
            .attr('x', ox)
            .attr('y', oy)
            .attr('width', me.stat_length * 1.6)
            .attr('height', 18)
            .style('fill', '#FFF')
            .style('stroke', 'transparent')
            .style('stroke-width', '0.5pt');

        item.append('line')
            .attr('x1', function (d, i) {
                return ox;
            })
            .attr('y1', function (d, i) {
                return oy + 9;
            })
            .attr('x2', function (d, i) {
                return ox + me.stepx * 4.75;
            })
            .attr('y2', function (d, i) {
                return oy + 9;
            })
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')
            .style("stroke-dasharray", '2 7');


        item.append('text')
            .attr("x", ox)
            .attr("y", oy)
            .attr("dy", 10)
            .style("text-anchor", 'start')
            .style("font-family", function () {
                return (power ? me.user_font : me.base_font);
                //return (power ? 'NothingYouCouldDo' : 'Titre');
            })
            .style("font-size", me.medium_font_size + 'px')
            .style("fill", function () {
                return (power ? me.user_fill : me.draw_fill);
            })
            .style("stroke", function () {
                return (power ? me.user_stroke : me.draw_stroke);
            })
            .style("stroke-width", '0.5pt')
            .text(function () {
                return name.charAt(0).toUpperCase() + name.slice(1);
            })
        let max = me.stat_max;
        if (value > me.stat_max) {
            max = me.stat_max * 2;
        }

        let dots = item.append('g')
            .attr('class', 'dots ' + type)
            .selectAll("g")
            .data(d3.range(0, max, 1));
        dots.enter()
            .append('circle')
            .attr('cx', function (d) {
                let cx = ox + me.stepx * 5 + (d % me.stat_max) * ((me.dot_radius) * 2);
                //                 if (d>=me.stat_max){
                //                     cx = ox+me.stepx*4+(d%me.stat_max)*((me.dot_radius)*2);
                //                 }
                return cx;
            })
            .attr('cy', function (d) {
                let cy = oy + me.dot_radius / 2;
                if (max > me.stat_max) {
                    cy -= me.dot_radius;
                }

                if (d >= me.stat_max) {
                    cy += +me.dot_radius / 2 + 2;
                }
                return cy;
            })
            .attr('r', function (d) {
                return (d >= me.stat_max ? me.dot_radius - 2 : me.dot_radius - 2);
            })
            .style('fill', function (d) {
                return (d < value ? me.user_fill : "white");
            })
            .style('stroke', function (d) {
                return me.draw_stroke;
            })
            .style('stroke-width', '1.5pt');
    }

    drawPages() {
        let me = this;
    }

    powerStat(name, ox, oy, type, statcode, source) {
        let me = this;
        if (name == '') {
            me.reinHagenStat('   ', 0, ox, oy, type, statcode, source)
        } else {
            let words = name.split(' (');
            let power = words[0];
            let val = (words[1].split(')'))[0];
            if (type == 'flaw') {
                power = power + ' -F-'
            }
            me.reinHagenStat(power, val, ox, oy, type, statcode, source, power = true)
        }
    }


    statText(name, value, ox, oy, type, statcode, source, fat = false, mono = false) {
        let me = this;
        let item = source.append('g')
            .attr('class', type);
        item.append('rect')
            .attr('x', ox)
            .attr('y', oy)
            .attr('width', me.stat_length * 1.6)
            .attr('height', 18)
            .style('fill', 'transparent')
            .style('stroke', 'transparent')
            .style('stroke-width', '0.5pt');
        item.append('line')
            .attr('x1', function (d, i) {
                return ox;
            })
            .attr('y1', function (d, i) {
                return oy + 9;
            })
            .attr('x2', function (d, i) {
                return ox + me.stepx * 6;
            })
            .attr('y2', function (d, i) {
                return oy + 9;
            })
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.5pt')
            .style("stroke-dasharray", '2 7');

        item.append('text')
            .attr("x", ox)
            .attr("y", oy)
            .attr("dy", 10)
            .style("text-anchor", 'start')
            .style("font-family", me.base_font)
            .style("font-size", me.medium_font_size + 'px')
            .style("fill", me.draw_fill)
            .style("stroke", me.draw_stroke)
            .style("stroke-width", '0.5pt')
            .text(function () {
                return name.charAt(0).toUpperCase() + name.slice(1);
            });

        if (fat) {
            item.append('text')
                .attr("x", ox + me.stepx * 6)
                .attr("y", oy)
                .attr("dy", 10)
                .style("text-anchor", 'end')
                .style("font-family", function (d) {
                    return (mono == true ? me.mono_font : me.user_font);
                })
                .style("font-size", (me.medium_font_size * 1.25) + 'px')
                .style("fill", me.user_fill)
                .style("stroke", me.user_stroke)
                .style("stroke-width", '0.5pt')
                .text(function () {
                    return value;
                });
        } else {
            item.append('text')
                .attr("x", ox + me.stepx * 6)
                .attr("y", oy)
                .attr("dy", 10)
                .style("text-anchor", 'end')
                .style("font-family", function (d) {
                    return (mono == true ? me.mono_font : me.user_font);
                })
                .style("font-size", me.medium_font_size + 'px')
                .style("fill", me.user_fill)
                .style("stroke", me.user_stroke)
                .style("stroke-width", '0.5pt')
                .text(function () {
                    return value;
                });
        }
    }

    title(name, ox, oy, source) {
        let me = this;
        let item = source.append('g');
        item.append('text')
            .attr("x", ox)
            .attr("y", oy)
            .attr("dy", 10)
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.big_font_size + 'px')
            .style("fill", '#111')
            .style("stroke", '#888')
            .style("stroke-width", '0.5pt')
            .text(function () {
                return name.charAt(0).toUpperCase() + name.slice(1);
            })

    }

    gaugeStat(name, value, ox, oy, source, withTemp = false, automax = false, max = 10) {
        let me = this;
        let type = name;
        let item = source.append('g');
        let lines = 1;
        let tempmax = max;

        item.append('text')
            .attr("x", ox)
            .attr("y", oy)
            .attr("dy", 10)
            .style("text-anchor", 'middle')
            .style("font-family", me.title_font)
            .style("font-size", me.big_font_size + 'px')
            .style("fill", '#111')
            .style("stroke", '#888')
            .style("stroke-width", '0.5pt')
            .text(function () {
                return name.charAt(0).toUpperCase() + name.slice(1);
            });
        if (automax) {
            tempmax = (Math.round(value / 10) + 1) * 10;
            lines = tempmax / 10;
        }

        let dots = item.append('g')
            .attr('class', 'dots ' + type)
            .selectAll("g")
            .data(d3.range(0, tempmax, 1));
        let dot = dots.enter();
        dot.append('circle')
            .attr('cx', function (d) {
                let cx = ox + (((d % 10)) - 4.5) * ((me.dot_radius * 2 + 1) * 2);
                //                 if (d>=10){
                //                     cx = ox+((d-10)-4.5)*((me.dot_radius+1)*2);
                //                 }
                return cx;
            })
            .attr('cy', function (d) {
                let cy = oy + 0.3 * me.stepx + me.dot_radius;
                if (d >= 10) {
                    cy += me.dot_radius * 2;
                }
                return cy;
            })
            .style('fill', function (d) {
                return (d < value ? me.user_fill : "white");
            })
            .attr('r', me.dot_radius)
            .style('stroke', me.draw_stroke)
            .style('stroke-width', '1pt');
        dot.append('rect')
            .attr('x', function (d) {
                let cx = ox + ((d % 10) - 4.5) * ((me.dot_radius * 2 + 1) * 2) - me.dot_radius;
                return cx;
            })
            .attr('y', function (d) {
                let cy = oy + 0.3 * me.stepx + me.dot_radius - me.dot_radius + (me.dot_radius * 2 + 2) * lines + 2;
                if (d >= 10) {
                    cy += me.dot_radius * 2 + 5;
                }
                return cy;
            })
            .attr('width', me.dot_radius * 2)
            .attr('height', me.dot_radius * 2)
            .style('fill', function (d) {
                return (withTemp ? 'white' : 'transparent');
            })
            .style('stroke', function (d) {
                return (withTemp ? me.draw_stroke : 'transparent');
            })
            .style('stroke-width', '0.5pt');

    }

    fillAttributes(basey) {
        let me = this;
        let ox = 0;
        let oy = basey;
        let stat = 'attribute';

        oy -= 0.5 * me.stepy;

        me.statText('Name', me.data['name'], ox + me.stepx * 2, oy, 'name', 'name', me.character, true);
        me.statText('Nature', me.data['nature'], ox + me.stepx * 9, oy, 'nature', 'nature', me.character);
        if (me.data["creature"] == 'kindred') {
            me.statText('Age/R(E)', me.data['age'] + "/" + me.data['trueage'] + " (" + me.data['embrace'] + "A.D)", ox + me.stepx * 16, oy, 'age', 'age', me.character);
        } else {
            me.statText('Age', me.data['age'], ox + me.stepx * 16, oy, 'age', 'age', me.character);
        }
        oy += 0.5 * me.stepy;
        if (me.data['player'] == '') {
            me.statText('Player', "Storyteller Character", ox + me.stepx * 2, oy, 'player', 'player', me.character);
        } else {
            me.statText('Player', me.data['player'], ox + me.stepx * 2, oy, 'player', 'player', me.character);
        }
        me.statText('Demeanor', me.data['demeanor'], ox + me.stepx * 9, oy, 'demeanor', 'demeanor', me.character);
        me.statText('Sex', (me.data['sex'] ? 'male' : 'female'), ox + me.stepx * 16, oy, 'sex', 'sex', me.character);

        oy += 0.5 * me.stepy;
        me.statText('Chronicle', me.data['chronicle'], ox + me.stepx * 2, oy, 'chronicle', 'chronicle', me.character);
        if (me.data["creature"] == 'kindred') {
            me.statText('Position', me.data['position'], ox + me.stepx * 9, oy, 'group', 'group', me.character);
        } else {
            me.statText('Residence', me.data['residence'], ox + me.stepx * 9, oy, 'group', 'group', me.character);
        }
        me.statText('Concept', me.data['concept'], ox + me.stepx * 16, oy, 'concept', 'concept', me.character);

        oy += 0.5 * me.stepy;
        me.statText('Creature', me.data['creature'].charAt(0).toUpperCase() + me.data['creature'].slice(1), ox + me.stepx * 2, oy, 'chronicle', 'chronicle', me.character);

        if (me.data["creature"] == 'kindred') {
            if (me.data["faction"] == 'Sabbat') {
                me.statText('Pack', me.data['groupspec'], ox + me.stepx * 9, oy, 'group', 'group', me.character);
            } else {
                me.statText('Coterie', me.data['groupspec'], ox + me.stepx * 9, oy, 'group', 'group', me.character);
            }
            me.statText('Clan', me.data['family'], ox + me.stepx * 16, oy, 'concept', 'concept', me.character);
        } else if (me.data["creature"] == 'garou') {
            me.statText('Pack', me.data['groupspec'], ox + me.stepx * 9, oy, 'group', 'group', me.character);
            me.statText('Totem', me.data['sire'], ox + me.stepx * 16, oy, 'concept', 'concept', me.character);
        }

        if (me.data["creature"] == 'kindred') {
            oy += 0.5 * me.stepy;
            me.statText('Faction', me.data['faction'], ox + me.stepx * 2, oy, 'faction', 'faction', me.character);
            me.statText('Territory', me.data['territory'], ox + me.stepx * 9, oy, 'Terri', 'territor', me.character);
            me.statText('Weakness', me.data['weakness'], ox + me.stepx * 16, oy, 'weakness', 'weakness', me.character);

            oy += 1.0 * me.stepy;
        } else {
            oy += 1.5 * me.stepy;
        }
        me.title('Physical (' + me.data['total_physical'] + ')', ox + me.stepx * 5, oy, me.character);
        me.title('Social (' + me.data['total_social'] + ')', ox + me.stepx * 12, oy, me.character);
        me.title('Mental (' + me.data['total_mental'] + ')', ox + me.stepx * 19, oy, me.character);

        oy += 0.5 * me.stepy;
        ox = 2 * me.stepx;
        // [0, 1, 2, 3, 4, 5, 6, 7, 8].forEach(function (d) {
        //     let x = ox + me.stepx * 7 * ((Math.round((d + 2) / 3)) - 1);
        //     let y = oy + 0.5 * me.stepy * ((d + 3) % 3);
        //     me.reinHagenStat(me.config['labels'][stat + 's'][d], me.data[stat + d], x, y, stat, stat + d, me.character);
        // });

    }

    fillAbilities(basey) {
        let me = this;
        let ox = 0;
        let oy = basey;
        let stat = '';

        me.title('Talents (' + me.data['total_talents'] + ')', ox + me.stepx * 5, oy, me.character);
        me.title('Skills (' + me.data['total_skills'] + ')', ox + me.stepx * 12, oy, me.character);
        me.title('Knowledges (' + me.data['total_knowledges'] + ')', ox + me.stepx * 19, oy, me.character);

        oy += 0.5 * me.stepy;

        stat = 'talent';
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(function (d) {
            let x = ox + me.stepx * 2;
            let y = oy + 0.5 * me.stepy * (d);
            me.reinHagenStat(me.config['labels'][stat + 's'][d], me.data[stat + d], x, y, stat, stat + d, me.character);
        });
        stat = 'skill';
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(function (d) {
            let x = ox + me.stepx * 9;
            let y = oy + 0.5 * me.stepy * (d);
            me.reinHagenStat(me.config['labels'][stat + 's'][d], me.data[stat + d], x, y, stat, stat + d, me.character);
        });
        stat = 'knowledge';
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(function (d) {
            let x = ox + me.stepx * 16;
            let y = oy + 0.5 * me.stepy * (d);
            me.reinHagenStat(me.config['labels'][stat + 's'][d], me.data[stat + d], x, y, stat, stat + d, me.character);
        });
    }

    fillAdvantages(basey) {
        let me = this;
        let ox = 0;
        let oy = basey;
        let stat = '';

        me.title('Backgrounds (' + me.data['total_backgrounds'] + ')', ox + me.stepx * 5, oy, me.character);
        if (me.data['creature'] == 'garou') {
            me.title('Gifts (' + me.data['total_traits'] + ')', ox + me.stepx * 12, oy, me.character);

        } else if (me.data['creature'] == 'kindred') {
            me.title('Disciplines (' + me.data['total_traits'] + ')', ox + me.stepx * 12, oy, me.character);
            me.title('Virtues', ox + me.stepx * 19, oy, me.character);

        } else {
            me.title('Other Traits', ox + me.stepx * 12, oy, me.character);
            if ((me.data['creature'] == 'mortal')) {
                me.title('Virtues', ox + me.stepx * 19, oy, me.character);
            }
        }
        oy += 0.5 * me.stepy;


        stat = 'background';
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(function (d) {
            let x = ox + me.stepx * 2;
            let y = oy + 0.5 * me.stepy * (d);
            me.reinHagenStat(me.config['labels'][stat + 's'][d], me.data[stat + d], x, y, stat, stat + d, me.character);
        });

        stat = 'trait';
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(function (d) {
            let x = ox + me.stepx * 9;
            let y = oy + 0.5 * me.stepy * (d);
            me.powerStat(me.data[stat + d], x, y, stat, stat + d, me.character);
        });

        stat = 'virtue';
        let levels = [];
        if (me.data['creature'] == 'garou') {
            oy -= me.stepy * 0.5;
            levels = ['Glory', 'Honor', 'Wisdom'];
            [0, 1, 2].forEach(function (d) {
                let x = ox + me.stepx * 19;
                let y = oy + 1.20 * me.stepy * (d);
                me.gaugeStat(levels[d], me.data[levels[d].toLowerCase()], x, y, me.character, true, false);
            });
        } else {
            levels = ['Conscience', 'Self-Control', 'Courage'];
            [0, 1, 2].forEach(function (d) {
                let x = ox + me.stepx * 16;
                let y = oy + 0.5 * me.stepy * (d);
                me.reinHagenStat(levels[d], me.data[stat + d], x, y, stat, stat + d, me.character);
            });

        }


        if (me.data['creature'] == 'garou') {

            let breeds = ['Homid', 'Metis', 'Lupus'];
            let auspices = ['Ragabash', 'Theurge', 'Philodox', 'Galliard', 'Ahroun'];
            oy += 3.75 * me.stepy;
            me.statText('Breed', breeds[me.data['breed']], ox + me.stepx * 16, oy, 'breed', 'breed', me.character);
            oy += 0.5 * me.stepy;
            me.statText('Auspice', auspices[me.data['auspice']], ox + me.stepx * 16, oy, 'auspice', 'auspice', me.character);
            oy += 0.5 * me.stepy;
            me.statText('Tribe', me.data['family'], ox + me.stepx * 16, oy, 'tribe', 'tribe', me.character);
            oy += 0.5 * me.stepy;
            me.reinHagenStat('Rank', me.data['rank'], ox + me.stepx * 16, oy, 'rank', 'rank', me.character);

        } else if (me.data['creature'] == 'kindred') {
            oy += 2 * me.stepy;
            me.statText('Generation', 13 - me.data['background3'] + 'th', ox + me.stepx * 16, oy, 'gener', 'gener', me.character);
            oy += 0.5 * me.stepy;
            me.statText('Sire', me.data['sire_name'], ox + me.stepx * 16, oy, 'sire', 'sire', me.character);
        }
    }


    drawHealth(basey) {
        let me = this;
        let ox = 0;
        let oy = basey;
        me.title('Health', ox + me.stepx * 19, oy, me.character);
        oy += me.stepy * 0.8;
        let h = me.character.append('g')
            .selectAll('g')
            .data(me.health_levels);
        let x = h.enter();
        x.append('line')
            .attr('x1', function (d, i) {
                return ox + me.stepx * 16;
            })
            .attr('y1', function (d, i) {
                return oy + i * me.stepy * 0.6;
            })
            .attr('x2', function (d, i) {
                return ox + me.stepx * 22;
            })
            .attr('y2', function (d, i) {
                return oy + i * me.stepy * 0.6;
            })
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .style("stroke-dasharray", '2 7');
        x.append('text')
            .attr('x', function (d, i) {
                return ox + me.stepx * 16;
            })
            .attr('y', function (d, i) {
                return oy + i * me.stepy * 0.6;
            })
            .style("text-anchor", 'start')
            .style("font-family", me.base_font)
            .style("font-size", me.medium_font_size + 'px')
            .style("fill", me.draw_fill)
            .style("stroke", me.draw_stroke)
            .style("stroke-width", '0.5pt')
            .text(function (d) {
                let words = d.split('/');
                return words[0];
            });
        x.append('text')
            .attr('x', function (d, i) {
                return ox + me.stepx * 19;
            })
            .attr('y', function (d, i) {
                return oy + i * me.stepy * 0.6;
            })
            .style("text-anchor", 'middle')
            .style("font-family", 'Titre')
            .style("font-size", me.medium_font_size + 'px')
            .style("fill", me.draw_fill)
            .style("stroke", me.draw_stroke)
            .style("stroke-width", '0.5pt')
            .text(function (d) {
                let words = d.split('/');
                if (words[1] == 'X') {
                    return '';
                }
                return words[1];
            });
        x.append('rect')
            .attr('x', function (d, i) {
                return ox + me.stepx * 22 - me.dot_radius * 2;
            })
            .attr('y', function (d, i) {
                return oy + i * me.stepy * 0.6 - me.dot_radius * 2;
            })
            .attr('width', me.dot_radius * 2)
            .attr('height', me.dot_radius * 2)
            .style("fill", "white")
            .style("stroke", me.draw_stroke)
            .style("stroke-width", '0.5pt');

    }


    fillOther(basey) {
        let me = this;
        let ox = 0;
        let oy = basey;
        let stat = '';
        me.title('Merits/Flaws', ox + me.stepx * 5, oy, me.character);
        oy += 0.5 * me.stepy;

        let merits_flaws = [];
        stat = 'merit';
        let idx = 0;
        [0, 1, 2, 3, 4].forEach(function (d) {
            if (me.data[stat + d] != '') {
                merits_flaws.push({
                    'idx': idx,
                    'class': 'merit',
                    'id': 'merit' + d
                });
                idx++;
            }
        });
        stat = 'flaw';
        [0, 1, 2, 3, 4].forEach(function (d) {
            if (me.data[stat + d] != '') {
                merits_flaws.push({
                    'idx': idx,
                    'class': 'flaw',
                    'id': 'flaw' + d
                });
                idx++;
            }
        });
        // Merits/Flaws
        _.forEach(merits_flaws, function (d, idx) {
            let x = ox + me.stepx * 2;
            let y = oy + 0.5 * me.stepy * (idx);
            me.powerStat(me.data[d['id']], x, y, d['class'], d['id'], me.character);
        });


        oy = basey;
        me.gaugeStat('Willpower', me.data['willpower'], ox + me.stepx * 12, oy, me.character, true);
        if (me.data['creature'] == 'garou') {
            oy += 1.7 * me.stepy;
            me.gaugeStat('Rage', me.data['rage'], ox + me.stepx * 12, oy, me.character, true);
            oy += 1.5 * me.stepy;
            me.gaugeStat('Gnosis', me.data['gnosis'], ox + me.stepx * 12, oy, me.character, true);
        }
        if (me.data['creature'] == 'kindred') {
            oy += 1.7 * me.stepy;
            me.gaugeStat('Humanity', me.data['humanity'], ox + me.stepx * 12, oy, me.character);
            oy += 1.5 * me.stepy;
            me.gaugeStat('Blood Pool', me.data['bloodpool'], ox + me.stepx * 12, oy, me.character, true, true, 20);

        }
        oy = basey;
        me.drawHealth(oy);
    }

    fillSpecial(basey) {
        let me = this;
        let ox = 0;
        let oy = basey;
        let stat = '';
        me.title('Specialities', ox + me.stepx * 5, oy, me.character);
        me.title('Action Shortcuts', ox + me.stepx * 12, oy, me.character);
        if (me.data['creature'] == 'garou') {
            me.title('Many Forms', ox + me.stepx * 19, oy, me.character);
        }
        oy += 0.5 * me.stepy;
        stat = 'speciality';
        me.config['specialities'].forEach(function (d, idx) {
            let x = ox + me.stepx * 2;
            let y = oy + 0.5 * me.stepy * (idx);
            me.statText(d, '', x, y, stat, stat + idx, me.character);
        });
        stat = 'shortcuts';
        me.config['shortcuts'].forEach(function (d, idx) {
            let x = ox + me.stepx * 9 + Math.floor(idx / 7) * me.stepx * 7;
            let y = oy + 0.5 * me.stepy * (idx % 7);
            let w = d.split('=');

            me.statText(w[0], w[1], x, y, stat, stat + idx, me.character);
        });

        if (me.data['creature'] == 'garou') {
            me.config["many_forms"] = [{
                'form': 'homid',
                'motherform': true,
                'size': 1.00,
                'weight': 1.00,
                'changes': {
                    'attribute0': 0,
                    'attribute1': 0,
                    'attribute2': 0,
                    'attribute3': 0,
                    'attribute4': 0,
                    'attribute5': 0,
                }
            }, {
                'form': 'glabro',
                'motherform': false,
                'size': 1.25,
                'weight': 1.50,
                'changes': {
                    'attribute0': 2,
                    'attribute1': 0,
                    'attribute2': 2,
                    'attribute3': 0,
                    'attribute4': -1,
                    'attribute5': -1
                }
            }, {
                'form': 'crinos',
                'motherform': false,
                'size': 1.50,
                'weight': 2.00,
                'changes': {
                    'attribute0': 4,
                    'attribute1': 1,
                    'attribute2': 3,
                    'attribute3': 0,
                    'attribute4': -3,
                    'attribute5': -10
                }
            }, {
                'form': 'hispo',
                'motherform': false,
                'size': 1.25,
                'weight': 2.00,
                'changes': {
                    'attribute0': 3,
                    'attribute1': 2,
                    'attribute2': 3,
                    'attribute3': 0,
                    'attribute4': -3,
                    'attribute5': 0
                }
            },

                {
                    'form': 'lupus',
                    'motherform': false,
                    'size': 0.5,
                    'weight': 0.5,
                    'changes': {
                        'attribute0': 1,
                        'attribute1': 2,
                        'attribute2': 2,
                        'attribute3': 0,
                        'attribute4': -3,
                        'attribute5': 0
                    }
                },
            ]
            let bonuses = "";
            let ax = ox + me.stepx * 16;
            let ay = oy + 0.5 * me.stepy * (0);
            me.statText("Attributes", " St De St Ch Ma Ap", ax, ay, 'fl', 'fl', me.character, false, true);
            me.config['many_forms'].forEach(function (d, idx) {
                ax = ox + me.stepx * 16;
                ay = oy + 0.5 * me.stepy * (idx + 1);
                bonuses = "";
                let list = d['changes'];

                _.forEach(list, function (v, k) {
                    let da = parseInt(me.data[k] + v);
                    if (da < 0) {
                        da = 0;
                    }
                    bonuses += " " + da + ".";
                });
                me.statText(d['form'], bonuses, ax, ay, d['form'], d['form'], me.character, false, true);
            });
        }


    }

    formatXml(xml) {
        var formatted = '';
        xml = xml.replace(/[\u00A0-\u2666]/g, function (c) {
            return '&#' + c.charCodeAt(0) + ';';
        })
        var reg = /(>)(<)(\/*)/g;
        /**/
        xml = xml.replace(reg, '$1\r\n$2$3');
        var pad = 0;
        jQuery.each(xml.split('\r\n'), function (index, node) {
            var indent = 0;
            if (node.match(/.+<\/\w[^>]*>$/)) {
                indent = 0;
            } else if (node.match(/^<\/\w/)) {
                if (pad != 0) {
                    pad -= 1;
                }
            } else if (node.match(/^<\w[^>]*[^\/]>.*$/)) {
                indent = 1;
            } else {
                indent = 0;
            }

            var padding = '';
            for (var i = 0; i < pad; i++) {
                padding += '  ';
            }

            formatted += padding + node + '\r\n';
            pad += indent;
        });

        return formatted;
    }


    addButton(num, txt) {
        let me = this;
        let ox = 28 * me.stepy;
        let oy = 2 * me.stepy;
        let button = me.back.append('g')
            .attr('class', 'do_not_print')
            .on('click', function (d) {
                if (num == 0) {
                    me.saveSVG();
                } else if (num == 1) {
                    me.savePNG();
                } else if (num == 2) {
                    me.createPDF();
                } else if (num == 3) {
                    me.editCreature();
                } else if (num == 4) {
                    me.page = 0;
                    me.perform(me.data)
                } else if (num == 5) {
                    me.page = 1;
                    me.perform(me.data)
                } else if (num == 6) {
                    me.page = 2;
                    me.perform(me.data)
                }
            })
        button.append('rect')
            .attr('id', "button" + num)
            .attr('x', ox + me.stepx * (-0.8))
            .attr('y', oy + me.stepy * (num - 0.4))
            .attr('width', me.stepx * 1.6)
            .attr('height', me.stepy * 0.8)
            .style('fill', '#CCC')
            .style('stroke', '#111')
            .style('stroke-width', '1pt')
            .attr('opacity', 1.0)
            .style('cursor', 'pointer')
            .on('mouseover', function (d) {
                me.svg.select('#button' + num).style("stroke", "#A22");
            })
            .on('mouseout', function (d) {
                me.svg.select('#button' + num).style("stroke", "#111");
            })

        ;
        button.append('text')
            .attr('x', ox)
            .attr('y', oy + me.stepy * num)
            .attr('dy', 5)
            .style('font-family', me.title_font)
            .style('text-anchor', 'middle')
            .style("font-size", me.medium_font_size + 'px')
            .style('fill', '#000')
            .style('cursor', 'pointer')
            .style('stroke', '#333')
            .style('stroke-width', '0.5pt')
            .attr('opacity', 1.0)
            .text(txt)
            .on('mouseover', function (d) {
                me.svg.select('#button' + num).style("stroke", "#A22");
            })
            .on('mouseout', function (d) {
                me.svg.select('#button' + num).style("stroke", "#111");
            })

        ;
    }

    saveSVG() {
        let me = this;
        me.svg.selectAll('.do_not_print').attr('opacity', 0);
        let base_svg = d3.select("#d3area svg").html();
        let flist = '<style>';
        for (let f of me.config['fontset']) {
            flist += '@import url("https://fonts.googleapis.com/css2?family=' + f + '");';
        }
        flist += '</style>';

        let exportable_svg = '<?xml version="1.0" encoding="UTF-8" ?> \
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"> \
<svg class="crossover_sheet" \
xmlns="http://www.w3.org/2000/svg" version="1.1" \
xmlns:xlink="http://www.w3.org/1999/xlink"> \
' + flist + base_svg + '</svg>';
        let fname = me.data['rid']+"_"+me.page + ".svg"
        let nuke = document.createElement("a");
        nuke.href = 'data:application/octet-stream;base64,' + btoa(me.formatXml(exportable_svg));
        nuke.setAttribute("download", fname);
        nuke.click();
        me.svg.selectAll('.do_not_print').attr('opacity', 1);
    }

    createPDF() {
        let me = this;
        me.svg.selectAll('.do_not_print').attr('opacity', 0);
        let base_svg = d3.select("#d3area svg#sheet").html();
        let flist = '<style>';
        console.log(me.config['fontset']);
        for (let f of me.config['fontset']) {

            flist += '@import url("https://fonts.googleapis.com/css2?family=' + f + '");';
        }
        flist += '</style>';
        let lpage = "";
        let exportable_svg = '<?xml version="1.0" encoding="UTF-8" ?> \
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"> \
<svg class="crossover_sheet" \
xmlns="http://www.w3.org/2000/svg" version="1.1" \
xmlns:xlink="http://www.w3.org/1999/xlink" width="' + me.width + '" height="' + me.height + '"> \
' + flist + base_svg + '</svg>';


        lpage = "_" + (me.page + 1);

        let svg_name = "character_sheet" + me.data['rid'] + lpage + ".svg"
        let pdf_name = "character_sheet" + me.data['rid'] + lpage + ".pdf"
        let sheet_data = {
            'pdf_name': pdf_name,
            'svg_name': svg_name,
            'svg': exportable_svg
        }
        me.svg.selectAll('.do_not_print').attr('opacity', 1);
        $.ajax({
            url: 'ajax/character/svg2pdf/' + me.data['rid'] + '/',
            type: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data: sheet_data,
            dataType: 'json',
            success: function (answer) {
                console.log("PDF generated for [" + me.data['rid'] + "]...")
            },
            error: function (answer) {
                console.error('Error generating the PDF...');
                console.error(answer);
            }
        });
    }

    wrap(txt_src, y_met, y_coe, x_off, y_off, width, font = 'default') {
        let me = this;
        if (font == 'default') {
            font = me.user_font;
        }
        let tgt = d3.select(this);
        tgt.attr('x', function (d) {
            return x_off;
        })
            .attr('y', function (d) {
                return y_off + d[y_met] * y_coe * me.stepy;
            })
            .attr('dx', 0)
            .attr('dy', 0)
            .text(function (d) {
                return d[txt_src];
            })
            .style("text-anchor", 'start')
            .style("font-family", font)
            .style("font-size", me.small_font_size + 'pt')
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
            .style("stroke-width", '0.05pt');
        let words = tgt.text().split(/\s+/).reverse(),
            word,
            line = [],
            lineNumber = 0,
            lineHeight = me.small_font_size * 1.15,
            x = tgt.attr("x"),
            y = tgt.attr("y");
        tgt.text(null);
        let tspan = tgt.append("tspan")
            .attr("x", function (d) {
                return x_off;
            })
            .attr('y', function (d) {
                return y_off + d[y_met] * y_coe * me.stepy;
            });

        while (word = words.pop()) {
            line.push(word);
            tspan.text(line.join(" "));
            if (tspan.node().getComputedTextLength() > width * me.stepy) {
                line.pop();
                tspan.text(line.join(" "));
                line = [word];
                tspan = tgt.append("tspan")
                    .attr("x", function (d) {
                        return x_off;
                    })
                    .attr('y', function (d) {
                        return y_off + d[y_met] * y_coe * me.stepy;
                    })
                    .attr("dy", ++lineNumber * lineHeight)
                    .style("font-size", me.small_font_size + 'pt')
                    .style("stroke-width", '0.05pt')
                    .text(word);
            }
        }
        // return (lineNumber);
    }

    zoomActivate() {
        let me = this;
        me.zoom = d3.zoom()
            .scaleExtent([0.25, 4])
            .on('zoom', function (event) {
                me.svg.attr('transform', event.transform)
            });
        me.vis.call(me.zoom);
    }


}

function

wrap(text, width, stacked = false) {
    let font = "Gochi Hand",
        user_fill = '#A8A',
        user_stroke = '#828',
        small_font_size = 8,
        base_y = 0,
        stackedHeight = 0;
    text.each(function () {
        let tgt = d3.select(this),
            words = tgt.text().split(/\s+/).reverse(),
            word,
            line = [],
            lineNumber = 0,
            x = tgt.attr("x"),
            y = tgt.attr("y"),
            font_size = 10,
            lineHeight = font_size * 1.8;
        let tspan = tgt.text(null).append("tspan")
            .attr("x", x)
            .attr('y', y);

        while (word = words.pop()) {
            line.push(word);
            tspan.text(line.join(" "));
            if (tspan.node().getComputedTextLength() > width) {
                line.pop();
                tspan.text(line.join(" "));
                line = [word];
                tspan = tgt.append("tspan")
                    .attr("x", x)
                    .attr('y', y)
                    .attr("dy", ++lineNumber * lineHeight)
                    .style("font-size", font_size)
                    .style("stroke-width", '0.05pt')
                    .text(word)
            }
        }
    });
}