init python:
    
    class hermione_character_face(silver_character_face):
        description = ""
        id = 0
        
        eyes = ""
        eye_color = ""
        nose = ""
        cheeks = ""
        mouth = ""
        lipstick = ""
        tears = ""
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def set(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def getLayers(self, parent):
            layers = []
            if self.cheeks != "":
                layers.append(parent.root+"body/face/cheeks/"+self.cheeks)
            if self.nose != "":
                layers.append(parent.root+"body/face/nose/"+self.nose)
            if self.mouth != "":
                layers.append(parent.root+"body/face/mouth/"+self.lipstick+"/"+self.mouth)
            if self.eyes != "":
                layers.append(parent.root+"body/face/eyes/"+parent.eye_color+"/"+self.eyes)
            if self.tears != "":
                layers.append(parent.root+"body/face/tears/"+self.tears)
            return layers
    
    class hermione_character_chibi(silver_character_chibi):
        level_ref = [
        ["01_hp/16_hermione_chibi/walk/h_walk_n_01.png","ch_hem blink_n","ch_hem blink_n_flip","ch_hem walk_n","ch_hem walk_n_flip"],
        ["01_hp/16_hermione_chibi/walk/h_walk_a_01.png","ch_hem blink_a","ch_hem blink_a_flip","ch_hem walk_a","ch_hem walk_a_flip"],
        ["01_hp/16_hermione_chibi/walk/h_walk_d_01.png","ch_hem blink_d","ch_hem blink_d_flip","ch_hem walk_d","ch_hem walk_d_flip"],
        ["01_hp/16_hermione_chibi/walk/h_walk_e_01.png","ch_hem blink_e","ch_hem blink_e_flip","ch_hem walk_e","ch_hem walk_e_flip"],
        ["01_hp/16_hermione_chibi/walk/h_walk_f_01.png","ch_hem blink_f","ch_hem blink_f_flip","ch_hem walk_f","ch_hem walk_f_flip"],
        ["01_hp/16_hermione_chibi/walk/h_walk_g_01.png","ch_hem blink_g","ch_hem blink_g_flip","ch_hem walk_g","ch_hem walk_g_flip"],
        ["01_hp/16_hermione_chibi/walk/h_walk_h_01.png","ch_hem blink_h","ch_hem blink_h_flip","ch_hem walk_h","ch_hem walk_h_flip"]
        ]
        
        def setLevel(self, level):
            if level >= 0 and level < len(self.level_ref):
                self.stand_img = self.level_ref[level][0]
                self.blink_img = self.level_ref[level][1]
                self.blink_img_f = self.level_ref[level][2]
                self.walk_img = self.level_ref[level][3]
                self.walk_img_f = self.level_ref[level][4]
    
    class hermione_character_uniform(sliver_character_uniform):
        level_ref = [["",""],[1,1],[2,1],[3,2],[4,3],[5,4],[6,4]]
        
        bot_color = ""
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def setLevel(self, level):
            if level >= 0 and level < len(self.level_ref):
                self.top = self.level_ref[level][0]
                self.bot = self.level_ref[level][1]
        
        def getLayers(self, parent):
            layers = []
            if self.panties != "" and self.wear_panties and not self.wear_bot:
                layers.append(parent.root+"clothes/underwear/"+self.panties)
            if self.bra != "" and self.wear_bra and not self.wear_top:
                layers.append(parent.root+"clothes/underwear/"+self.bra)
            if self.bot != "" and self.wear_bot:
                layers.append(parent.root+"clothes/uniform/bot/"+self.bot_color+str(self.bot)+".png")
            if self.top != "" and self.wear_top:
                layers.append(parent.root+"clothes/uniform/top/"+str(self.top)+".png")
            return layers
    

label __init_variables:
    
    $ reset_char_obj = True
    if not hasattr(renpy.store,'hermione_SC') or reset_char_obj: #important!
        $ hermione_SC = silver_character(
            root = "01_hp/13_characters/hermione/",
            
            xpos = 370,
            ypos = 0,
            
            name = "Hermione Granger",
            pet_name = "Miss Granger",
            genie_name = "Professor",
            
            eye_color = "brown",
        
            screen = "test_herm_obj",
            screen_head = "test_herm_head_obj",
            
            chibi = hermione_character_chibi(
                stand_img = "01_hp/16_hermione_chibi/walk/h_walk_a_01.png",
                blink_img = "ch_hem blink_a",
                blink_img_f = "ch_hem blink_a_flip",
                walk_img = "ch_hem walk_a",
                walk_img_f = "ch_hem walk_a_flip",
                xpos = 0,
                ypos = 250
            ),
            
            char_ref = Character('Hermione', color="#402313", window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed", window_right_padding=250),
            h_char_ref = Character('Hermione', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed"),
            
            body = sliver_character_body(
                head = sliver_character_head(
                    expression = None,
                    base = "hermione_base.png",
                    hair = "A_1.png",
                    cheeks = "",
                    glasses = ""
                ),
                left_arm = "left_1.png",
                right_arm = "right_1.png",
                torso = "torso.png",
                torso_pressed = "torso_pressed.png",
                abdomen = "abdomen.png",
                legs = "legs_1.png"
                
            ),
            
            uniform = hermione_character_uniform(
                top = 1,
                bot = 1,
                panties = "base_panties_1.png",
                bra = "base_bra_white_1.png",
            ),
            acc = ""
        )
    $ hermione_SC.faces = getCharacterFaces('hermione_face',hermione_character_face)
    $ hermione_SC.setFace(1)
    
    $ h_whoring = 0
    $ h_reputation = 21
    
    $ hermione_zorder = 5
    
    $ hg_NoPanties_lvl = 9
    
    if not hasattr(renpy.store,'hermione_xpos'          ): #important!
        $ hermione_xpos         = 370
    if not hasattr(renpy.store,'hermione_ypos'          ): #important!
        $ hermione_ypos         = 0
    if not hasattr(renpy.store,'hermione_head_xpos'     ): #important!
        $ hermione_head_xpos    = 390
    if not hasattr(renpy.store,'hermione_head_ypos'     ): #important!
        $ hermione_head_ypos    = 235
    
    $ hermione_body             = "01_hp/13_characters/hermione/body/face/preset/body_01.png"
    $ hermione_tears            = "01_hp/13_characters/hermione/body/face/tears/00_blank.png"
    $ hermione_base             = "01_hp/13_characters/hermione/body/base/hermione_base.png"
    $ hermione_legs             = "01_hp/13_characters/hermione/body/legs/legs_1.png"
    $ hermione_breasts          = "01_hp/13_characters/hermione/body/breasts/breasts_nipfix.png"
    $ hermione_left_arm         = "01_hp/13_characters/hermione/body/arms/left/left_1.png"
    $ hermione_right_arm        = "01_hp/13_characters/hermione/body/arms/right/right_1.png"
    $ hermione_emote            = "01_hp/13_characters/emote/00_blank.png"
    
    $ h_body                    = "body_01"
    $ h_tears                   = "00_blank"
    
    $ h_display_tears = False
    
    if not hasattr(renpy.store,'hermione_hair_a'        ): #important!
        $ hermione_hair_a       = "01_hp/13_characters/hermione/body/head/A_1.png"
    if not hasattr(renpy.store,'hermione_hair_b'        ): #important!
        $ hermione_hair_b       = "01_hp/13_characters/hermione/body/head/A_1_2.png"
    if not hasattr(renpy.store,'h_hair_style'           ): #important!
        $ h_hair_style          = "A"
    if not hasattr(renpy.store,'h_hair_color'           ): #important!
        $ h_hair_color          = 1
    
    if not hasattr(renpy.store,'h_skirt_color'          ): #important!
        $ h_skirt_color         = ""

    #Toggle
    if not hasattr(renpy.store,'hermione_wear_top'): #important!
        $ hermione_wear_top         = True
        $ hermione_wear_bra         = True
        $ hermione_wear_skirt       = True
        $ hermione_wear_panties     = True

        $ hermione_wear_neckwear    = False
        $ hermione_wear_belt        = False
        $ hermione_wear_gloves      = False
        $ hermione_wear_stockings   = False
        $ hermione_wear_robe        = False

        $ hermione_badges           = False
    
    #Toggle Save-State
    if not hasattr(renpy.store,'h_request_wear_top'): #important!
        $ h_request_wear_top        = False
        $ h_request_wear_bra        = False
        $ h_request_wear_bottom     = False
        $ h_request_wear_panties    = False


    #Init Clothing
    if not hasattr(renpy.store,'reset_her_clothing'): #important!
        $ reset_her_clothing        = True

    #Top
    if not hasattr(renpy.store,'hermione_top') or reset_her_clothing: #important!
        $ hermione_top              = "01_hp/13_characters/hermione/clothes/uniform/top_1.png"
        $ h_top                     = "uni_top_1"


    #Bottom
    if not hasattr(renpy.store,'hermione_skirt') or reset_her_clothing: #important!
        $ hermione_skirt            = "01_hp/13_characters/hermione/clothes/uniform/skirt_1.png"
        $ h_skirt                   = "uni_skirt_1"


    #Underwear
    if not hasattr(renpy.store,'hermione_bra') or reset_her_clothing: #important!
        $ hermione_bra              = "01_hp/13_characters/hermione/clothes/underwear/base_bra_white_1.png"
        $ h_bra                     = "bra_white"

        $ hermione_panties          = "01_hp/13_characters/hermione/clothes/underwear/base_panties_1.png"
        $ h_panties                 = "panties_white"

        $ h_corset                  = "00_blank"
        $ h_garterbelt              = "00_blank"

    $ hermione_panties_overlay      = "01_hp/13_characters/hermione/overlays/00_blank.png"


    #Other Clothing
    if not hasattr(renpy.store,'hermione_neckwear') or reset_her_clothing: #important!
        $ hermione_neckwear         = "01_hp/13_characters/hermione/clothes/neckwear/neck_scarf_gryff.png"
        $ h_neckwear                = "neck_scarf_gryff"

        $ hermione_belt             = "01_hp/13_characters/hermione/clothes/belts/00_blank.png"
        $ h_belt                    = "00_blank"

        $ hermione_gloves           = "01_hp/13_characters/hermione/clothes/gloves/gloves_gryff.png"
        $ h_gloves                  = "gloves_gryff"

        $ hermione_stockings        = "01_hp/13_characters/hermione/clothes/stockings/stockings_gryff.png"
        $ h_stockings               = "stockings_gryff"

        $ hermione_robe             = "01_hp/13_characters/hermione/clothes/robe/gryff_robe.png"
        $ h_robe                    = "gryff_robe"


    #Accessories
        $ hermione_badge            = "01_hp/13_characters/hermione/accessories/badges/spew_badge.png"
        $ h_badge                   = "spew_badge"    
    
        $ hermione_piercings        = []
        $ hermione_tattoos          = []

    $ reset_her_clothing = False

    $ h_breasts                  = "breasts_nipfix"
    $ h_bra_nip_fix              = ["bra_silk_black","bra_lace_turquoise","bra_french_maid", "bra_bikini_string_black", "bra_bikini_string_blue", "bra_leather_black", "underwear_misc_insulating_tape", "underwear_misc_bra_white_ripped", "underwear_misc_heart_pasties", "underwear_misc_seethru_bandeau"]
    
    $ h_bra_top_fix              = ["normal_pullover_sexy", "normal_pullover", "normal_purple_sweater", "uni_top_1", "uni_top_2", "uni_top_3", "uni_top_4", "uni_top_5", "uni_top_6", "uni_top_cheer_gryff_skimpy", "uni_top_cheer_gryff", "uni_top_cheer_slyth_skimpy", "uni_top_cheer_slyth"]

    $ h_can_color                = ["A","B"]

    
    if not hasattr(renpy.store,'hermione_perm_expand'): #important!
        $ hermione_perm_expand       = False
        $ hermione_breasts_perm_expand       = False
        $ hermione_ass_perm_expand       = False
    
    ## Chibi Vars
    $ hermione_chibi_stand       = "01_hp/16_hermione_chibi/walk/h_walk_a_01.png"
    $ hermione_chibi_stand_nude  = "01_hp/16_hermione_chibi/walk/h_walk_n_01.png"
    $ hermione_chibi_blink       = "ch_hem blink_a"
    $ hermione_chibi_blink_f     = "ch_hem blink_a_flip"
    $ hermione_chibi_walk        = "ch_hem walk_a"
    $ hermione_chibi_walk_f      = "ch_hem walk_a_flip"
    $ hermione_chibi_zorder      = 3
    
    ## Action Vars
    if not hasattr(renpy.store,'hermione_action'): #important!
        $ hermione_action        = False
    
    $ hermione_action_bra        = hermione_bra
    $ hermione_action_panties    = hermione_panties
    $ hermione_action_top        = hermione_top
    $ hermione_action_skirt      = hermione_skirt
    
    $ hermione_action_left_arm = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    $ hermione_action_right_arm = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    $ hermione_action_a = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    $ hermione_action_b = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    
    $ h_action_right_arm       = "00_blank.png"
    $ h_action_left_arm        = "00_blank.png"
    $ h_action_a               = "00_blank.png"
    $ h_action_b               = "00_blank.png"
    
    $ h_action_show_arms       = False
    $ h_action_show_bra        = True
    $ h_action_show_panties    = True
    $ h_action_show_top        = True
    $ h_action_show_skirt      = True
    
    ## Emote Vars
    $ hermione_emote_anger     = False
    $ hermione_emote_exclam    = False
    $ hermione_emote_hearts    = False
    $ hermione_emote_question  = False
    $ hermione_emote_sweat     = False
    $ hermione_emote_suprize   = False
    $ hermione_anger           = ["body_51","body_76","body_86","body_110","body_218","body_351","body_346","body_345","body_343","body_317","body_309","head_exp/24"]
    $ hermione_exclam          = ["head_exp/30"]
    $ hermione_hearts          = []
    $ hermione_question        = []
    $ hermione_sweat           = ["body_24","body_34","body_57","body_108","body_208","body_340","head_exp/9"]
    $ hermione_suprize         = ["body_80","body_80b","body_335"]
    
    
    
    $ u_h_animation            = ""
    $ u_h_animation_paused     = ""
    $ u_h_ani_xpos             = 0
    $ u_h_ani_ypos             = 0
    
    
    
    ## Custom Clothes/Outfits Vars
    if not hasattr(renpy.store,'custom_outfit'): #important!
        $ custom_outfit = 0
    if not hasattr(renpy.store,'hermione_costume'): #important!
        $ hermione_costume = False
    if not hasattr(renpy.store,'hermione_costume_action_a'): #important!
        $ hermione_costume_action_a = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    
    return
    
label her_main_new(text="",face=h_body, xpos = hermione_xpos, ypos = hermione_ypos):
    $ wt_herm = hermione_SC
    hide screen test_herm_obj
    if xpos != wt_herm.xpos:
        $ wt_herm.xpos = xpos
    if ypos != wt_herm.ypos:
        $ wt_herm.ypos = ypos
    if face != wt_herm.body.head.face.id:
        $ wt_herm.setFace(face)
    show screen test_herm_obj
    with d2
    if text != "":
        $ renpy.say(her, text)
    return
    
    
label her_main(text="",face=h_body,tears="", xpos = hermione_xpos, ypos = hermione_ypos):
    hide screen hermione_main
    if her_main_smooth_transition: #when moving her xpos #looks better
        with d3
        pause 0.1
        $ her_main_smooth_transition = False
    else:
        pass
    if xpos != hermione_xpos:
        if xpos == 370:
            $ hermione_xpos = 510
        elif xpos == 120:
            $ hermione_xpos = 140
        else:
            $ hermione_xpos = xpos
    if ypos != hermione_ypos:
        $ hermione_ypos = ypos
    if face != h_body:
        $ h_body = face
        #$ hermione_body = her_path + str(face) + ".png"
    $ h_tears = tears
    call h_update
    show screen hermione_main
    if not wardrobe_active: #No Dissolve in wardrobe
        with d3
    if text != "":
        $ renpy.say(her,text)
    return
    
label her_head(text="",face=h_body,tears=""):
    if face != h_body:
        $ h_body = face
        # $ h_body = her_path + str(face) + ".png"
    $ h_tears = tears
    call h_update
    show screen hermione_head #h_head2
    if text != "":
        $ renpy.say(her2,text)
    hide screen hermione_head #h_head2
    return
    
label her_kneel(text="",face=h_body,tears=""):
    if face != h_body:
        $ h_body = face
        # $ h_body = her_path + str(face) + ".png"
    $ h_tears = tears
    call h_update
    show screen hermione_kneel #h_head2
    if text != "":
        $ renpy.say(her,text)
    return
