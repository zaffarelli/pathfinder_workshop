class CrossOverSheet extends WawwodSheet {
    constructor(data, parent, collector) {
        super(data, parent, collector);
        this.init();
    }

    init() {
        super.init();
        let me = this;
    }

    drawPages() {
        super.drawPages();
        let me = this
        let lines = me.back.append('g');
        if (me.page === 0) {
            me.midline(4, 0.5, 23.5);
            me.crossline(0.5, 0.5, 1.0);
            me.midline(0.5, 0.5, 1.0);
            me.crossline(23.5, 35.5, 35.0);
            me.midline(35.5, 23.0, 23.5);


            // Title
            let txt = me.sheet_type("Pathfinder").toUpperCase();


            me.daddy = lines;


            me.characterInfo();


            me.drawAbilities(0.5, 5)
            me.drawHP(6.7, 5)
            me.drawInit(6.7, 10)
            me.drawSpeed(14, 5)
            me.drawAC(0.5, 11.5)
            me.drawSavingThrows(0.5, 15)
            me.drawAttack(0.5, 18.5)
            me.drawWeapons(0.5, 22)
            me.drawLanguages(14, 32.5)

            me.boxField("SKILLS", 0, 14, 7.5, 9.5, 0.8, true, "");
            let skill_ystart = 9

            _.forEach(me.data.all_ranks, function (v, k) {
                me.skillField(14 * me.stepx, skill_ystart * me.stepy, v);
                skill_ystart += 0.65;
            });

            me.stdField("Total Skill Ranks ", me.data['ranks_summary'].toUpperCase(), 14 * me.stepx, 32 * me.stepy, 6);
            me.decorationText(4, 2.25, 3, 'middle', me.logo_font, me.fat_font_size, me.shadow_fill, me.shadow_stroke, 4, "Pathfinder", me.back);
            me.decorationText(4, 2.25, 0, 'middle', me.logo_font, me.fat_font_size, me.draw_fill, me.draw_stroke, 0.5, "Pathfinder", me.back);
            me.decorationText(4, 2.75, 0, 'middle', me.title_font, me.big_font_size, me.draw_fill, me.draw_stroke, 0.5, "Role Playing Game", me.back);
            me.decorationText(4, 3.5, 0, 'middle', me.title_font, me.medium_font_size, me.draw_fill, me.draw_stroke, 0.5, "Character Sheet", me.back);
        } else if (me.page === 1) {
            me.midline(4, 0.5, 23.5);
            me.crossline(0.5, 0.5, 1.0);
            me.midline(0.5, 0.5, 1.0);
            me.crossline(23.5, 35.5, 35.0);
            me.midline(35.5, 23.0, 23.5);
            me.decorationText(4, 2.25, 3, 'middle', me.logo_font, me.fat_font_size, me.shadow_fill, me.shadow_stroke, 4, "Pathfinder", me.back);
            me.decorationText(4, 2.25, 0, 'middle', me.logo_font, me.fat_font_size, me.draw_fill, me.draw_stroke, 0.5, "Pathfinder", me.back);
            me.decorationText(4, 2.75, 0, 'middle', me.title_font, me.big_font_size, me.draw_fill, me.draw_stroke, 0.5, "Role Playing Game", me.back);
            me.decorationText(4, 3.5, 0, 'middle', me.title_font, me.medium_font_size, me.draw_fill, me.draw_stroke, 0.5, "Equipment Sheet", me.back);
            me.daddy = lines;
            me.characterInfo();
            me.drawClassData(13.5, 4.75);
            me.drawGear(0.5, 4.75);
            me.drawFeats(13.5, 7.5);
            me.drawSpecialAbilities(13.5, 17.0);
            me.drawMoney(13.5, 30.5);
            me.drawEncumberance(0.5, 30.5);
            me.drawSpecial(1.5, 35.5);

        } else if (me.page === 2) {
            me.midline(4, 0.5, 23.5);
            me.crossline(0.5, 0.5, 1.0);
            me.midline(0.5, 0.5, 1.0);
            me.crossline(23.5, 35.5, 35.0);
            me.midline(35.5, 23.0, 23.5);
            me.decorationText(4, 2.25, 3, 'middle', me.logo_font, me.fat_font_size, me.shadow_fill, me.shadow_stroke, 4, "Pathfinder", me.back);
            me.decorationText(4, 2.25, 0, 'middle', me.logo_font, me.fat_font_size, me.draw_fill, me.draw_stroke, 0.5, "Pathfinder", me.back);
            me.decorationText(4, 2.75, 0, 'middle', me.title_font, me.big_font_size, me.draw_fill, me.draw_stroke, 0.5, "Role Playing Game", me.back);
            me.decorationText(4, 3.5, 0, 'middle', me.title_font, me.medium_font_size, me.draw_fill, me.draw_stroke, 0.5, "Spells Sheet", me.back);
            me.daddy = lines;
            me.characterInfo();
            me.drawSpellbook(0.5, 5, me.data['spellbook'])
        }
        if (me.page > 0) {
            // me.decorationText(10.5, 2.25, 0, 'start', me.user_font, me.medium_font_size, me.user_fill, me.user_stroke, 0.5, me.data["name"] + " (p." + (me.page + 1) + ")", me.back);
        }
        me.decorationText(21.5, 1.75, 0, 'middle', me.title_font, me.medium_font_size, me.draw_fill, me.draw_stroke, 0.5, me.pre_title, me.back);
        me.decorationText(21.5, 2.25, 0, 'middle', me.title_font, me.medium_font_size, me.draw_fill, me.draw_stroke, 0.5, me.post_title, me.back);
        me.decorationText(1.5, 35.8, -16, 'start', me.base_font, me.small_font_size, me.draw_fill, me.draw_stroke, 0.5, me.guideline, me.back);
        me.decorationText(22.4, 35.5, 5, 'end', me.title_font, me.small_font_size, me.draw_fill, me.draw_stroke, 0.5, "Zaff's Pathfinder 1E Character Sheet 2022 (Version:0.7) Generated with Pathfinder Workshop", me.back);
        // me.decorationText(22.5, 34.8, 0, 'end', me.base_font, me.small_font_size, me.draw_fill, me.draw_stroke, 0.5, 'Challenge:' + me.data['freebies'], me.back);
    }

    drawButtons() {
        let me = this;
        me.addButton(0, 'Save SVG');
        me.addButton(1, 'Save PNG');
        me.addButton(2, 'Save PDF');
        me.addButton(4, 'Page 1');
        me.addButton(5, 'Page 2');
        me.addButton(6, 'Page 3');
        me.addButton(7, 'Page 4');
    }

    characterInfo() {
        let me = this;
        me.stdField("Character Name", me.data['name'].toUpperCase(), 8, 1.5, 6);
        me.stdField("Alignment", me.data['alignment_str'], 14.5, 1.5, 2);
        me.stdField("Player", me.data['player'], 17, 1.5, 6.5);

        me.stdField("Character Class and Level", me.data.ccl, 8, 2.5, 7.5);
        me.stdField("Deity", me.data['deity'], 16, 2.5, 3);
        me.stdField("Homeland", me.data['homeland'], 19.5, 2.5, 4);

        me.stdField("Race", me.data.race_name, 8, 3.5, 3);
        me.stdField("Size", me.data.size, 11.5, 3.5, 2.5);
        me.stdField("Gender", me.data.gender_str, 14.5, 3.5, 2.5);
        me.stdField("Age", me.data.age, 17.5, 3.5, 1);
        me.stdField("Height", me.data.height_foot + " (" + me.data.height_m + ")", 19, 3.5, 2);
        me.stdField("Weight", me.data.weight_lbs + " (" + me.data.weight_kg + ")", 21.5, 3.5, 2);

    }

    drawAbilities(ox, y) {
        let me = this;
        let oy = y
        me.boxField("STR", 0, ox, oy, 2, 0.8, true, "strength");
        me.boxField("Ability Score", "STR", ox + 2, oy, 1);
        me.boxField("Ability Modifier", "STR_mod", ox + 3, oy, 1);
        me.boxField("Temp Score", 0, ox + 4, oy, 1);
        me.boxField("Temp Modifier", 0, ox + 5, oy, 1);
        oy += 1
        me.boxField("DEX", 0, ox, oy, 2, 0.8, true, "dexterity");
        me.boxField("", "DEX", ox + 2, oy, 1);
        me.boxField("", "DEX_mod", ox + 3, oy, 1);
        me.boxField("", 0, ox + 4, oy, 1);
        me.boxField("", 0, ox + 5, oy, 1);
        oy += 1
        me.boxField("CON", 0, ox, oy, 2, 0.8, true, "constitution");
        me.boxField("", "CON", ox + 2, oy, 1);
        me.boxField("", "CON_mod", ox + 3, oy, 1);
        me.boxField("", 0, ox + 4, oy, 1);
        me.boxField("", 0, ox + 5, oy, 1);
        oy += 1
        me.boxField("INT", 0, ox, oy, 2, 0.8, true, "intelligence");
        me.boxField("", "INT", ox + 2, oy, 1);
        me.boxField("", "INT_mod", ox + 3, oy, 1);
        me.boxField("", 0, ox + 4, oy, 1);
        me.boxField("", 0, ox + 5, oy, 1);
        oy += 1
        me.boxField("WIS", 0, ox, oy, 2, 0.8, true, "wisdom");
        me.boxField("", "WIS", ox + 2, oy, 1);
        me.boxField("", "WIS_mod", ox + 3, oy, 1);
        me.boxField("", 0, ox + 4, oy, 1);
        me.boxField("", 0, ox + 5, oy, 1);
        oy += 1
        me.boxField("CHA", 0, ox, oy, 2, 0.8, true, "charisma");
        me.boxField("", "CHA", ox + 2, oy, 1);
        me.boxField("", "CHA_mod", ox + 3, oy, 1);
        me.boxField("", 0, ox + 4, oy, 1);
        me.boxField("", 0, ox + 5, oy, 1);
    }

    drawHP(ox, oy) {
        let me = this;
        // HP
        me.boxField("HP", "", ox, oy, 2, 0.8, true, "Hit Points");
        me.boxField("Total", "hp", ox + 2, oy, 2);
        me.boxField("Damage Resistance", 0, ox + 4, oy, 3);
        me.boxField("Wounds/Current HP", 0, ox, oy + 1, 7, 1.8, false, "", true);
        me.boxField("Nonlethal Damage", 0, ox, oy + 3, 7, 1.4, false, "", true);
    }


    drawLanguages(ox, oy) {
        let me = this;
        // Languages
        me.boxField("Languages", "", ox, oy, 9.5, 0.8, true, "");
        me.boxField("", "languages", ox, oy + 1, 9.5, 1.8);

    }

    drawClassData(ox, y) {
        let me = this;
        let oy = y;
        // Languages
        me.boxField("Experience Points", "", ox, oy, 3, 0.8, true, "");
        me.boxField("XP", "current_xp", ox + 3, oy, 3);
        me.boxField("Next Level", "next_level", ox + 6, oy, 4);
        oy += 1.4;
        me.boxField("Favored Class", "", ox, oy, 4, 0.8, true, "");
        me.boxField("", "", ox + 4, oy, 4, 0.8, false, "");
        me.boxField("Skills Points", "", ox + 8, oy, 1, 0.8, false, "Skills Points");
        me.boxField("Hit Points", "", ox + 9, oy, 1, 0.8, false, "Hit Points");

    }

    drawGear(ox, y) {
        let me = this;
        let oy = y;
        let txt = "", txt2 = "";
        // Languages
        me.boxField("Gear/Equipment", "", ox, oy, 12.5, 0.8, true, "");
        oy += 0.9
        _.forEach([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], function (v, k) {
            oy += 0.8
            me.smallField(k + 1, ox, oy, 10.5);
            if (k == 0) {
                txt = "Weight";
                txt2 = "Value"
            } else {
                txt = txt2 = "";
            }

            me.boxField(txt, "", ox + 10.5, oy - 0.6, 1, 0.6, false, "");
            me.boxField(txt2, "", ox + 11.5, oy - 0.6, 1, 0.6, false, "");
        });
    }

    drawFeats(ox, y) {
        let me = this;
        let oy = y;
        let txt = ""
        // Languages
        me.boxField("Feats", "", ox, oy, 8, 0.8, true, "");
        me.boxField("Total", "nb_feats", ox + 8, oy, 2, 0.8, false, "");
        oy += 0.9
        console.log(me.data['feats_list'])
        let w = me.data['nb_feats'].split("+")
        let nb_feats = 0
        _.forEach(w, function (x) {
            nb_feats += parseInt(x)
        })
        _.forEach([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], function (v, k) {
            oy += 0.8
            txt = k + 1
            if (me.blank == false) {
                if (k < nb_feats) {
                    txt = me.data['feats_list'][k]
                }
            }

            me.smallField(txt, ox, oy, 10);

        });
    }

    drawSpecialAbilities(ox, y) {
        let me = this;
        let oy = y;
        let txt = "", txt2 = "";
        console.log(me.data['all_features'])
        me.boxField("Special Abilities", "", ox, oy, 10, 0.8, true, "");
        oy += 0.9
        _.forEach([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], function (v, k) {
            oy += 0.8
            txt = k + 1
            if (me.blank == false) {
                // if (k < me.data['all_features']['features'].length) {
                //     txt = me.data['all_features']['features'][k]
                // }
            }
            me.smallField(k + 1, ox, oy, 10);
        });
    }

    drawMoney(ox, y) {
        let me = this;
        let oy = y;
        let txt = "", txt2 = "";
        me.boxField("Money", "", ox, oy, 10, 0.8, true, "1 PP = 10 GP = 100 SP = 1000 CP");
        oy += 0.9
        _.forEach([{"type": "Platinium Coins"}, {"type": "Gold Coins"}, {"type": "Silver Coins"}, {"type": "Copper Coins"}], function (v, k) {
            oy += 0.8
            me.boxField(v["type"], "", ox, oy - 0.6, 3, 0.6, true, "");
            me.smallField("", ox + 3.5, oy, 4);
        });
    }

    drawEncumberance(ox, y) {
        let me = this;
        let oy = y;
        let txt = "", txt2 = "";
        me.boxField("Encumberance", "", ox, oy, 12.5, 0.8, true, "How much you can carry");
        oy += 0.9
        _.forEach([{"type": "Light Load"}, {"type": "Medium Load"}, {"type": "Heavy Load"}], function (v, k) {
            oy += 0.8
            me.boxField(v["type"], "", ox, oy - 0.6, 3, 0.6, true, "");
            me.smallField("", ox + 3.5, oy, 6);
        });
    }

    drawSpecial(ox, oy) {
        let me = this;
        let item = me.daddy.append('g')
            .attr('class', 'skill_text_grp');
        item.append('rect')
            .attr('x', function (d, i) {
                return ox * me.stepx;
            })
            .attr('y', function (d, i) {
                return (oy - 0.1) * me.stepy;
            })
            .attr('width', function (d, i) {
                return 0.2 * me.stepx;
            })
            .attr('height', function (d, i) {
                return 0.2 * me.stepy;
            })
            .style("fill", function (d, i) {
                return "transparent";
            })
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '1.0pt')
        ;
        item.append('text')
            .attr("x", (ox + 0.3) * me.stepx)
            .attr("y", oy * me.stepy)
            .attr("dy", "6pt")
            .style("text-anchor", 'start')
            .style("font-family", me.title_font)
            .style("font-size", me.tiny_font_size + 'pt')
            .style("fill", me.draw_fill)
            .style("stroke", me.shadow_stroke)
            .style("stroke-width", '0.5pt')
            .text("Check this box if you're deeply convinced Zaffarelli is the best DM ever. Your opinion matters.");
    }

    drawWeapons(ox, y) {
        let me = this;
        let oy = y;
        me.boxField("Weapons", "", ox, oy, 13, 0.8, true, "");
        oy += 1.5
        _.forEach(me.data.all_weapons, function (v, k) {
            if (k == 0) {
                me.boxField("Weapon", 0, ox, oy, 4, 0.8, false, "");
                me.boxField("Attack Bonus", 0, ox + 4, oy, 1);
                me.boxField("DMG", 0, ox + 5, oy, 2);
                me.boxField("Damage Bonus", 0, ox + 7, oy, 1);
                me.boxField("Weapon Type", 0, ox + 8, oy, 1);
                me.boxField("Range", 0, ox + 9, oy, 1);
                me.boxField("Ammoes", 0, ox + 10, oy, 1);
                me.boxField("Special", 0, ox + 11, oy, 2);
            } else {
                me.boxField("", 0, ox, oy, 4, 0.8, false, "");
                me.boxField("", 0, ox + 4, oy, 1);
                me.boxField("", 0, ox + 5, oy, 2);
                me.boxField("", 0, ox + 7, oy, 1);
                me.boxField("", 0, ox + 8, oy, 1);
                me.boxField("", 0, ox + 9, oy, 1);
                me.boxField("", 0, ox + 10, oy, 1);
                me.boxField("", 0, ox + 11, oy, 2);
            }
            oy += 1.1;
        });
    }

    drawInit(ox, oy) {
        let me = this;
        me.boxField("INITIATIVE", 0, ox, oy, 2, 0.8, true, "Modifier");
        me.boxField("Total", "init", ox + 2, oy, 2);
        me.floatingText(ox + 4.1, oy + 0.5, "=")
        me.boxField("Dex Modifier", "DEX_mod", ox + 4.2, oy, 1);
        me.floatingText(ox + 5.4, oy + 0.5, "+")
        me.boxField("Misc Modifier", "init_mod", ox + 5.6, oy, 1);
    }

    drawSpeed(ox, oy) {
        let me = this;
        // SPEED
        me.boxField("SPEED", "", ox, oy, 2, 0.8, true, "Feet");
        me.boxField("Land", "speed", ox + 2, oy, 2);
        me.boxField("Squares", "speed_sq", ox + 4, oy, 1);
        me.boxField("With Armor", "armor_speed", ox + 5, oy, 2);
        me.boxField("Squares", "armor_speed_sq", ox + 7, oy, 1);

        me.boxField("Fly", "fly_speed", ox, oy + 1.5, 2);
        me.boxField("Swim", "swim_speed", ox + 2, oy + 1.5, 2);
        me.boxField("Climb", "climb_speed", ox + 4, oy + 1.5, 2);
        me.boxField("Burrow", "burrow_speed", ox + 6, oy + 1.5, 2);

        me.boxField("Mods", 0, ox + 8, oy, 1.5, 2.3);

    }

    drawAC(ox, y) {
        let me = this;
        let oy = y;


        me.boxField("AC", 0, ox, oy, 2, 0.8, true, "armor class");
        me.boxField("Total", "AC", ox + 2, oy, 1);
        me.floatingText(ox + 3.5, oy + 0.5, "= 10 +")
        me.boxField("Armor Bonus", "AC_armor_bonus", ox + 4, oy, 1);
        me.floatingText(ox + 5, oy + 0.5, "+")
        me.boxField("Shield Bonus", "AC_shield_bonus", ox + 5, oy, 1);
        me.floatingText(ox + 6, oy + 0.5, "+")
        me.boxField("DEX Modifier", "DEX_mod", ox + 6, oy, 1);
        me.floatingText(ox + 7, oy + 0.5, "+")
        me.boxField("Size Modifier", "AC_size_modifier", ox + 7, oy, 1);
        me.floatingText(ox + 8, oy + 0.5, "+")
        me.boxField("Natural Armor", "AC_natural_armor", ox + 8, oy, 1);
        me.floatingText(ox + 9, oy + 0.5, "+")
        me.boxField("Deflection Bonus", "AC_deflection_bonus", ox + 9, oy, 1);
        me.floatingText(ox + 10, oy + 0.5, "+")
        me.boxField("Temp modifier", "AC_temp_modifier", ox + 10, oy, 1);
        me.boxField("Mods", 0, ox + 11, oy, 2, 2.8);
        oy += 1;
        me.boxField("Touch", 0, ox, oy, 2, 0.8, true, "armor class");
        me.boxField("", "touch_AC", ox + 2, oy, 1);
        me.floatingText(ox + 3.5, oy + 0.5, "= 10 +")
        // me.boxField("", "AC_armor_bonus", ox + 4, oy, 1);
        // me.floatingText(ox+5,oy+0.5,"+")
        // me.boxField("", "AC_shield_bonus", ox + 5, oy, 1);
        // me.floatingText(ox+6,oy+0.5,"+")
        me.boxField("", "DEX_mod", ox + 6, oy, 1);
        me.floatingText(ox + 7, oy + 0.5, "+")
        me.boxField("", "AC_size_modifier", ox + 7, oy, 1);
        // me.floatingText(ox+8,oy+0.5,"+")
        // me.boxField("", "AC_natural_armor", ox + 8, oy, 1);
        me.floatingText(ox + 9, oy + 0.5, "+")
        me.boxField("", "AC_deflection_bonus", ox + 9, oy, 1);
        me.floatingText(ox + 10, oy + 0.5, "+")
        me.boxField("", "AC_temp_modifier", ox + 10, oy, 1);
        oy += 1;
        me.boxField("Flat Footed", 0, ox, oy, 2, 0.8, true, "armor class");
        me.boxField("", "flatfooted_AC", ox + 2, oy, 1);
        me.floatingText(ox + 3.5, oy + 0.5, "= 10 +")
        me.boxField("", "AC_armor_bonus", ox + 4, oy, 1);
        me.floatingText(ox + 5, oy + 0.5, "+")
        me.boxField("", "AC_shield_bonus", ox + 5, oy, 1);
        me.floatingText(ox + 6, oy + 0.5, "+")
        // me.boxField("", "DEX_mod", ox + 6, oy, 1);
        // me.floatingText(ox+7,oy+0.5,"+")
        me.boxField("", "AC_size_modifier", ox + 7, oy, 1);
        me.floatingText(ox + 8, oy + 0.5, "+")
        me.boxField("", "AC_natural_armor", ox + 8, oy, 1);
        me.floatingText(ox + 9, oy + 0.5, "+")
        me.boxField("", "AC_deflection_bonus", ox + 9, oy, 1);
        me.floatingText(ox + 10, oy + 0.5, "+")
        me.boxField("", "AC_temp_modifier", ox + 10, oy, 1);

    }

    drawSavingThrows(ox, oy) {
        let me = this;
        me.boxField("Fortitude", 0, ox, oy, 2, 0.8, true, "Constitution");
        me.boxField("Total", "fortitude", ox + 2, oy, 1);
        me.floatingText(ox + 3, oy + 0.5, "=")
        me.boxField("Base Save", "base_fortitude", ox + 3, oy, 1);
        me.floatingText(ox + 4, oy + 0.5, "+")
        me.boxField("Ability Modifier", "fortitude_ability_mod", ox + 4, oy, 1);
        me.floatingText(ox + 5, oy + 0.5, "+")
        me.boxField("Magic Modifier", "fortitude_magic_mod", ox + 5, oy, 1);
        me.floatingText(ox + 6, oy + 0.5, "+")
        me.boxField("Misc Modifier", "fortitude_misc_mod", ox + 6, oy, 1);
        me.floatingText(ox + 7, oy + 0.5, "+")
        me.boxField("Temp Modifier", "fortitude_temp_mod", ox + 7, oy, 1);
        me.boxField("Mods", 0, ox + 8, oy, 5, 2.8);

        me.boxField("Reflex", 0, ox, oy + 1, 2, 0.8, true, "Dexterity");
        me.boxField("", "reflex", ox + 2, oy + 1, 1);
        me.floatingText(ox + 3, oy + 1.5, "=")
        me.boxField("", "base_reflex", ox + 3, oy + 1, 1);
        me.floatingText(ox + 4, oy + 1.5, "+")
        me.boxField("", "reflex_ability_mod", ox + 4, oy + 1, 1);
        me.floatingText(ox + 5, oy + 1.5, "+")
        me.boxField("", "reflex_magic_mod", ox + 5, oy + 1, 1);
        me.floatingText(ox + 6, oy + 1.5, "+")
        me.boxField("", "reflex_misc_mod", ox + 6, oy + 1, 1);
        me.floatingText(ox + 7, oy + 1.5, "+")
        me.boxField("", "reflex_temp_mod", ox + 7, oy + 1, 1);

        me.boxField("Will", 0, ox, oy + 2, 2, 0.8, true, "Wisdom");
        me.boxField("", "will", ox + 2, oy + 2, 1);
        me.floatingText(ox + 3, oy + 2.5, "=")
        me.boxField("", "base_will", ox + 3, oy + 2, 1);
        me.floatingText(ox + 4, oy + 2.5, "+")
        me.boxField("", "will_ability_mod", ox + 4, oy + 2, 1);
        me.floatingText(ox + 5, oy + 2.5, "+")
        me.boxField("", "will_magic_mod", ox + 5, oy + 2, 1);
        me.floatingText(ox + 6, oy + 2.5, "+")
        me.boxField("", "will_misc_mod", ox + 6, oy + 2, 1);
        me.floatingText(ox + 7, oy + 2.5, "+")
        me.boxField("", "will_temp_mod", ox + 7, oy + 2, 1);
    }

    drawAttack(ox, y) {
        let me = this;
        let oy = y;
        me.boxField("BAB", 0, ox, oy, 3, 0.8, true, "Base Attack Bonus");
        me.boxField("", "BAB", ox + 3, oy, 3);

        me.boxField("SR", 0, ox + 6, oy, 3, 0.8, true, "Spell Resistance");
        me.boxField("", "SR", ox + 9, oy, 4);


        oy += 1.4;
        me.boxField("CMB", 0, ox, oy, 3, 0.8, true, "Combat Maneuver Bonus");
        me.boxField("", "CMB", ox + 3, oy, 1);
        me.floatingText(ox + 4.5, oy + 0.5, "= ")
        me.boxField("BAB", "BAB", ox + 5, oy, 1);
        me.floatingText(ox + 6, oy + 0.5, "+")
        me.boxField("STR modifier", "STR_mod", ox + 6, oy, 1);
        // me.floatingText(ox+7,oy+0.5,"+")
        // me.boxField("DEX Modifier", "DEX_mod", ox + 7, oy, 1);
        me.floatingText(ox + 8, oy + 0.5, "+")
        me.boxField("Size Modifier", "AC_size_modifier", ox + 8, oy, 1);

        me.boxField("Mods", "", ox + 9, oy, 4, 1.8);


        oy += 1;
        me.boxField("CMD", 0, ox, oy, 3, 0.8, true, "Combat Maneuver Defense");
        me.boxField("", "CMD", ox + 3, oy, 1);
        me.floatingText(ox + 4.5, oy + 0.5, "= 10 +")
        me.boxField("", "BAB", ox + 5, oy, 1);
        me.floatingText(ox + 6, oy + 0.5, "+")
        me.boxField("", "STR_mod", ox + 6, oy, 1);
        me.floatingText(ox + 7, oy + 0.5, "+")
        me.boxField("DEX Modifier", "DEX_mod", ox + 7, oy, 1);
        me.floatingText(ox + 8, oy + 0.5, "+")
        me.boxField("", "AC_size_modifier", ox + 8, oy, 1);


    }

    drawSpellbook(x, y, spells_lists) {
        let me = this;
        let ox = x;
        let oy = y;
        console.log(spells_lists)
        _.forEach(spells_lists, function (list, li) {
            me.smallField("Spells as " + list.name, ox, oy, 11.5, true);

            oy += 0.6;
            ox += 1
            let txt = ""
            _.forEach(list.spd, function (spd, di) {
                // me.smallField("LVL "+di + " " + spd.spd, ox, oy, 0.5);
                txt = spd.spd
                if (spd.spd != '-') {
                    txt = parseInt(spd.spd) + spd.ability_bonus

                }
                me.boxField("Lvl " + spd.level.toString(), txt, ox, oy, 1, 0.8, false, spd.level, false, true);
                ox += 1;
            })
            ox = x;
            oy += 1.5;
            _.forEach(list.list, function (spell, si) {
                let desc = spell.short_description.replace("&nbsp;"," ")
                me.smallField(spell.name, ox, oy, 2.5);
                me.smallField(spell.level, (ox + 2.75), oy, 0.5);
                me.smallField(desc, (ox + 3.5), oy, 8);
                _.forEach([0,1,2,3,4,5], function (t, ti) {
                    me.boxField("", "", ox+11.5+0.25*t, oy-0.3, 0.4, 0.2, false, "", false, true);
                });
                oy += 0.5;
            })
        })
    }

    fillBackgroundNotes(oy) {
        let me = this;
        let box_spacing_y = 3.0;
        let background_note = me.character.append('g')
            .attr('class', 'background_notes')
        ;


        me.title('About Backgrounds', 5.5 * me.stepx, oy - 0.5 * me.stepy, background_note)

        let background_note_item = background_note.selectAll('background_note')
            .data(me.data['background_notes'])
        ;
        let background_note_in = background_note_item.enter()
            .append('g')
            .attr('class', 'background_note')
        ;
        background_note_in.append('rect')
            .attr("x", function (d) {
                return (1.75) * me.stepx;
            })
            .attr("y", function (d) {
                return oy + d['idx'] * box_spacing_y * me.stepy;
            })
            .attr("rx", "8pt")
            .attr("ry", "8pt")
            .attr("width", function (d) {
                return me.stepx * 7.5;
            })
            .attr("height", function (d) {
                return me.stepy * (box_spacing_y - 0.35);
            })
            .style("stroke", "#080808")
            .style("fill", "transparent")
        ;
        background_note_in.append('text')
            .attr("x", function (d) {
                return 5.5 * me.stepx;
            })
            .attr('y', function (d) {
                return oy + (d['idx'] * box_spacing_y + 0.30) * me.stepy;
            })
            .text(function (d) {
                return d['item']
            })
            .style('font-family', me.title_font)
            .style('font-size', me.medium_font_size)
            .style('text-anchor', "middle")
            .style("fill", me.draw_fill)
            .style("stroke", me.draw_stroke)
            .style("stroke-width", "0.05pt")
        ;
        let background_note_in_note = background_note_in.append('text')
            .attr("x", function (d) {
                return 2 * me.stepx;
            })
            .attr('y', function (d) {
                return oy + (d['idx'] * box_spacing_y + 0.75) * me.stepy;
            })
            .text(function (d) {
                return d['notes']
            })
            .style('font-family', me.user_font)
            .style('font-size', me.small_font_size)
            .style('text-anchor', "start")
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
            .style("stroke-width", "0.05pt");
        background_note_in_note.call(wrap, 7 * me.stepx)
    }


    fillTimeline(oy) {
        let me = this;
        let box_spacing_y = 3.0;
        let box_spacing_x = 11.0;
        let base_x = 10.25;
        let timeline = me.character.append('g')
            .attr('class', 'timeline')
        ;
        me.daddy = me.timeline;
        me.title('Timeline', (base_x + 6) * me.stepx, oy - 0.5 * me.stepy, timeline)

        let timeline_item = timeline.selectAll('timeline_event')
            .data(me.data['timeline'])
        ;
        let timeline_in = timeline_item.enter()
            .append('g')
            .attr('class', 'timeline_event')
        ;
        let timeline_in_rect = timeline_in.append('rect')
            .attr("x", function (d) {
                return (base_x) * me.stepx;
            })
            .attr("y", function (d) {
                return oy + d['idx'] * box_spacing_y * me.stepy;
            })
            .attr("width", function (d) {
                return me.stepx * (base_x + 2);
            })
            .attr("height", function (d) {
                return me.stepy * (box_spacing_y - 0.25);
            })
            .attr("rx", "8pt")
            .attr("ry", "8pt")
            .style("fill", "white")
            .style("stroke", "#808080")
        ;
        timeline_in.append('text')
            .attr("x", function (d) {
                return (base_x + 0.05) * me.stepx;
            })
            .attr('y', function (d) {
                return oy + (d['idx'] * box_spacing_y + 0.5) * me.stepy;
            })
            .text(function (d) {
                return d['date'] + ' - ' + d['item']
            })
            .style('font-family', me.user_font)
            .style('font-size', me.medium_font_size)
            .style('text-anchor', "start")
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
        let timeline_in_note = timeline_in.append('text')
            .attr('x', function (d) {
                return (base_x + 0.4) * me.stepx;
            })
            .attr('y', function (d) {
                return oy + 0.85 * me.stepy + d['idx'] * 3 * me.stepy;
            })
            .attr('dx', 0)
            .attr('dy', 0)
            .text(function (d) {
                return d['notes'];
            })
            .style("text-anchor", 'start')
            .style("font-family", me.user_font)
            .style("font-size", me.small_font_size)
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
            .style("stroke-width", '0.05pt')
        ;
        timeline_in_note.call(wrap, box_spacing_x * me.stepx, true);
    }

    fillDisciplinesNotes(oy) {
        let me = this;
        let box_spacing_y = 3.0;
        let box_spacing_x = 10.0;
        let base_x = 12.0;
        let d_notes = me.character.append('g')
            .attr('class', 'notes_on_disciplines')
        ;
        me.daddy = me.d_notes;
        me.title('About Disciplines', 17 * me.stepx, oy - 0.5 * me.stepy, d_notes)

        let d_notes_item = d_notes.selectAll('discipline_event')
            .data(me.data['disciplines_notes'])
        ;
        let d_notes_in = d_notes_item.enter()
            .append('g')
            .attr('class', 'discipline_event')
        ;
        let d_notes_in_rect = d_notes_in.append('rect')
            .attr("x", function (d) {
                return (base_x) * me.stepx;
            })
            .attr("y", function (d) {
                return oy + d['idx'] * 3.0 * me.stepy;
            })
            .attr("width", function (d) {
                return me.stepx * box_spacing_x;
            })
            .attr("height", function (d) {
                return me.stepy * (box_spacing_y - 0.25);
            })
            .attr("rx", "8pt")
            .attr("ry", "8pt")
            .style("fill", "white")
            .style("stroke", "#808080")
        ;
        d_notes_in.append('text')
            .attr("x", function (d) {
                return (base_x + 0.05) * me.stepx;
            })
            .attr('y', function (d) {
                return oy + (d['idx'] * box_spacing_y + 0.5) * me.stepy;
            })
            .text(function (d) {
                return me.as_dots(d['score']) + ' - ' + d['item'] + ' - ' + d['title']
            })
            .style('font-family', me.user_font)
            .style('font-size', me.medium_font_size)
            .style('text-anchor', "start")
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
        let d_notes_in_note = d_notes_in.append('text')
            .attr('x', function (d) {
                return (base_x + 0.4) * me.stepx;
            })
            .attr('y', function (d) {
                return oy + 0.85 * me.stepy + d['idx'] * box_spacing_y * me.stepy;
            })
            .attr('dx', 0)
            .attr('dy', 0)
            .text(function (d) {
                return d['notes'];
            })
            .style("text-anchor", 'start')
            .style("font-family", me.user_font)
            .style("font-size", me.small_font_size)
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
            .style("stroke-width", '0.05pt')
        ;
        d_notes_in_note.call(wrap, 9 * me.stepx, true);
    }

    fillNatureNotes(oy) {
        let me = this;
        let n_notes = me.character.append('g')
            .attr('class', 'not_on_nature')
        ;
        me.daddy = me.n_notes;
        me.title('About Nature & Demeanor', 6 * me.stepx, oy - 0.5 * me.stepy, n_notes)

        let n_notes_item = n_notes.selectAll('nature_event')
            .data(me.data['nature_notes'])
        ;
        let n_notes_in = n_notes_item.enter()
            .append('g')
            .attr('class', 'nature_event')
        ;
        let n_notes_in_rect = n_notes_in.append('rect')
            .attr("x", function (d) {
                return (1.5) * me.stepx;
            })
            .attr("y", function (d) {
                return oy + d['idx'] * 3.5 * me.stepy;
            })
            .attr("rx", "8pt")
            .attr("ry", "8pt")
            .attr("width", function (d) {
                return me.stepx * 9;
            })
            .attr("height", function (d) {
                return me.stepy * 3.25;
            })
            .style("fill", "white")
            .style("stroke", "#808080")
        ;
        n_notes_in.append('text')
            .attr("x", function (d) {
                return 1.75 * me.stepx;
            })
            .attr('y', function (d) {
                return oy + (d['idx'] * 3.5 + 0.5) * me.stepy;
            })
            .text(function (d) {
                return d['item']
            })
            .style('font-family', me.user_font)
            .style('font-size', me.medium_font_size)
            .style('text-anchor', "start")
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
        let n_notes_in_note = n_notes_in.append('text')
            .attr('x', function (d) {
                return 1.9 * me.stepx;
            })
            .attr('y', function (d) {
                return oy + 0.85 * me.stepy + d['idx'] * 3.5 * me.stepy;
            })
            .attr('dx', 0)
            .attr('dy', 0)
            .text(function (d) {
                return d['notes'];
            })
            .style("text-anchor", 'start')
            .style("font-family", me.user_font)
            .style("font-size", me.small_font_size)
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
            .style("stroke-width", '0.05pt')
        ;
        n_notes_in_note.call(wrap, 8.5 * me.stepx, true);
    }

    fillMeritsFlawsNotes(oy) {
        let me = this;
        let box_spacing_y = 3.0;
        let mf_note = me.character.append('g')
            .attr('class', 'mf_notes')
        ;


        me.title('About Merits & Flaws', 5.5 * me.stepx, oy - 0.5 * me.stepy, mf_note)

        let mf_note_item = mf_note.selectAll('background_note')
            .data(me.data['meritsflaws_notes'])
        ;
        let mf_note_in = mf_note_item.enter()
            .append('g')
            .attr('class', 'mf_note')
        ;
        mf_note_in.append('rect')
            .attr("x", function (d) {
                return (1.75) * me.stepx;
            })
            .attr("y", function (d) {
                return oy + d['idx'] * box_spacing_y * me.stepy;
            })
            .attr("rx", "8pt")
            .attr("ry", "8pt")
            .attr("width", function (d) {
                return me.stepx * 7.5;
            })
            .attr("height", function (d) {
                return me.stepy * (box_spacing_y - 0.35);
            })
            .style("stroke", "#080808")
            .style("fill", "transparent")
        ;
        mf_note_in.append('text')
            .attr("x", function (d) {
                return 5.5 * me.stepx;
            })
            .attr('y', function (d) {
                return oy + (d['idx'] * box_spacing_y + 0.30) * me.stepy;
            })
            .text(function (d) {
                return d['item'] + " (" + d['type'] + ": " + me.as_dots(d['value']) + ")"
            })
            .style('font-family', me.title_font)
            .style('font-size', me.medium_font_size)
            .style('text-anchor', "middle")
            .style("fill", me.draw_fill)
            .style("stroke", me.draw_stroke)
            .style("stroke-width", "0.05pt")
        ;
        let mf_note_in_note = mf_note_in.append('text')
            .attr("x", function (d) {
                return 2 * me.stepx;
            })
            .attr('y', function (d) {
                return oy + (d['idx'] * box_spacing_y + 0.75) * me.stepy;
            })
            .text(function (d) {
                return d['notes']
            })
            .style('font-family', me.user_font)
            .style('font-size', me.small_font_size)
            .style('text-anchor', "start")
            .style("fill", me.user_fill)
            .style("stroke", me.user_stroke)
            .style("stroke-width", "0.05pt");
        mf_note_in_note.call(wrap, 7 * me.stepx)
    }

    as_dots(value) {
        let str = ""
        for (let i = 0; i < value; i++) {
            str += "●"
        }
        for (let i = value; i < 5; i++) {
            str += "○"
        }
        return str
    }

    fillCharacter() {
        let me = this;
        if (me.page === 0) {
            me.fillAttributes(4 * me.stepy);
            me.fillAbilities(9.5 * me.stepy);
            me.fillAdvantages(16.5 * me.stepy);
            me.fillOther(23.5 * me.stepy);
            me.fillSpecial(30.5 * me.stepy);
        } else if (me.page === 1) {
            me.fillBackgroundNotes(4 * me.stepy);
            me.fillTimeline(4 * me.stepy);
        } else if (me.page === 2) {
            me.fillNatureNotes(4 * me.stepy);
            me.fillMeritsFlawsNotes(12 * me.stepy);
            me.fillDisciplinesNotes(4 * me.stepy);

        }
    }

    perform(character_data) {
        let me = this;
        me.data = character_data;
        me.guideline = me.data['guideline']
        me.drawWatermark();
        if (me.data['condition'] == "DEAD") {
            me.decorationText(12, 16, 0, 'middle', me.logo_font, me.fat_font_size * 3, me.shadow_fill, me.shadow_stroke, 0.5, "DEAD", me.back, 0.25);
        }
        // me.fillCharacter();
        me.drawButtons();
        me.zoomActivate();
    }

}

