screen hermione_main:
    tag hermione_main
    
    add hermione_base xpos hermione_xpos ypos hermione_ypos #Add the base body
    add hermione_legs xpos hermione_xpos ypos hermione_ypos
    
    if hermione_action and h_action_show_arms:
        add hermione_action_right_arm xpos hermione_xpos ypos hermione_ypos
    elif not hermione_action:
        add hermione_right_arm xpos hermione_xpos ypos hermione_ypos
    
    add hermione_breasts xpos hermione_xpos ypos hermione_ypos
    
    if hermione_action and h_action_show_arms:
        add hermione_action_left_arm xpos hermione_xpos ypos hermione_ypos
    elif not hermione_action:
        add hermione_left_arm xpos hermione_xpos ypos hermione_ypos
    
    add hermione_hair_a xpos hermione_xpos ypos hermione_ypos #Add the hair shadow
    add hermione_body xpos hermione_xpos ypos hermione_ypos
    add hermione_tears xpos hermione_xpos ypos hermione_ypos
    
  ### CLOTHES
    add hermione_stockings xpos hermione_xpos ypos hermione_ypos
    
    if hermione_dribble:
        add "01_hp/13_characters/hermione/body/legs/dripping.png" xpos hermione_xpos ypos hermione_ypos
    
    if not hermione_custom_outfit and not hermione_action:
        ### SKIRT
        if h_request_wear_panties or hermione_wear_panties:
            add hermione_panties xpos hermione_xpos ypos hermione_ypos # Add the panties
            add hermione_panties_overlay xpos hermione_xpos ypos hermione_ypos
        if hermione_wear_skirt:
            add hermione_skirt xpos hermione_xpos ypos hermione_ypos # Add the skirt

        ### TOP
        if hermione_wear_top:
            add hermione_top xpos hermione_xpos ypos hermione_ypos # Add the top
        elif hermione_wear_bra:
            add hermione_bra xpos hermione_xpos ypos hermione_ypos # Add the bra
    elif hermione_custom_outfit:
        add hermione_custom_a xpos hermione_xpos ypos hermione_ypos
        add hermione_custom_b xpos hermione_xpos ypos hermione_ypos
        add hermione_custom_c xpos hermione_xpos ypos hermione_ypos
        add hermione_custom_d xpos hermione_xpos ypos hermione_ypos
        add hermione_custom_e xpos hermione_xpos ypos hermione_ypos
        add hermione_custom_action_a xpos hermione_xpos ypos hermione_ypos
    
    add hermione_hair_b xpos hermione_xpos ypos hermione_ypos
    
    if hermione_action:
        if h_action_show_skirt:
            add hermiome_action_skirt xpos hermione_xpos ypos hermione_ypos
        elif h_action_show_panties or h_request_wear_panties:
            add hermiome_action_panties xpos hermione_xpos ypos hermione_ypos
        if h_action_show_top:
            add hermiome_action_top xpos hermione_xpos ypos hermione_ypos
        elif h_action_show_bra:
            add hermiome_action_bra xpos hermione_xpos ypos hermione_ypos
        add hermiome_action_a xpos hermione_xpos ypos hermione_ypos
        add hermiome_action_b xpos hermione_xpos ypos hermione_ypos
    
    if uni_sperm:
        add u_sperm xpos hermione_xpos ypos hermione_ypos
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "01_hp/13_hermione_main/auto_02.png" xpos hermione_xpos ypos hermione_ypos
    elif aftersperm: #Shows cum stains on Hermione's uniform.
        add "01_hp/13_hermione_main/auto_03.png" xpos hermione_xpos ypos hermione_ypos
    
    if hermione_badges and hermione_wear_top and not hermione_custom_outfit:
        add hermione_badge xpos hermione_xpos ypos hermione_ypos # add badge on top
        
    if hermione_wear_robe:
        add hermione_robe xpos hermione_xpos ypos hermione_ypos
    add hermione_emote xpos hermione_xpos ypos hermione_ypos
    
    
    ### ZORDER
    zorder hermione_zorder
    
screen hermione_head:
    tag hermione_head
    
    add hermione_base xpos hermione_head_xpos ypos hermione_head_ypos #Add the base body
    add hermione_legs xpos hermione_head_xpos ypos hermione_head_ypos
    add hermione_right_arm xpos hermione_head_xpos ypos hermione_head_ypos
    add hermione_breasts xpos hermione_head_xpos ypos hermione_head_ypos
    add hermione_left_arm xpos hermione_head_xpos ypos hermione_head_ypos
    add hermione_hair_a xpos hermione_head_xpos ypos hermione_head_ypos #Add the hair shadow
    
    add hermione_body xpos hermione_head_xpos ypos hermione_head_ypos
    add hermione_tears xpos hermione_head_xpos ypos hermione_head_ypos
    
  ### CLOTHES
    add hermione_stockings xpos hermione_head_xpos ypos hermione_head_ypos
    if not hermione_custom_outfit:
        ### SKIRT
        if hermione_wear_skirt:
            add hermione_skirt xpos hermione_head_xpos ypos hermione_head_ypos # Add the skirt
        elif hermione_wear_panties or h_request_wear_panties:
            add hermione_panties xpos hermione_head_xpos ypos hermione_head_ypos # Add the panties
        ### TOP
        if hermione_wear_top:
            add hermione_top xpos hermione_head_xpos ypos hermione_head_ypos # Add the top
        elif hermione_wear_bra:
            add hermione_bra xpos hermione_head_xpos ypos hermione_head_ypos # Add the bra
    else:
        add hermione_custom_a xpos hermione_head_xpos ypos hermione_head_ypos
        add hermione_custom_b xpos hermione_head_xpos ypos hermione_head_ypos
        add hermione_custom_c xpos hermione_head_xpos ypos hermione_head_ypos
        add hermione_custom_d xpos hermione_head_xpos ypos hermione_head_ypos
        add hermione_custom_e xpos hermione_head_xpos ypos hermione_head_ypos
        add hermione_custom_action_a xpos hermione_head_xpos ypos hermione_head_ypos
    
    add hermione_hair_b xpos hermione_head_xpos ypos hermione_head_ypos
    
    if uni_sperm:
        add u_sperm xpos hermione_head_xpos ypos hermione_head_ypos
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "01_hp/13_hermione_main/auto_02.png" xpos hermione_head_xpos ypos hermione_head_ypos
    elif aftersperm: #Shows cum stains on Hermione's uniform.
        add "01_hp/13_hermione_main/auto_03.png" xpos hermione_head_xpos ypos hermione_head_ypos
    
    if hermione_wear_robe:
        add hermione_robe xpos hermione_head_xpos ypos hermione_head_xpos
    add hermione_emote xpos hermione_head_xpos ypos hermione_head_ypos
    
    ### ZORDER
    zorder 8
    
    
label set_hermione_robe(robe = ""):
    hide screen hermione_main
    with d3
    call h_robe(robe)
    return
    
label h_robe(robe = ""):
    if robe == "":
        $ hermione_wear_robe = False
    else:
        $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/"+str(robe)
        $ hermione_wear_robe = True
    return
    
    
## Outfit Blocks
label set_hermione_outfit(outfit_id):
    show screen blkfade
    hide screen hermione_main
    with d3
    call h_outfit(outfit_id)
    pause .5
    hide screen blkfade
    with d5
    return
    
label h_outfit(outfit_id):
    $ custom_outfit = outfit_id
    if custom_outfit == 0:
        $ hermione_custom_outfit = False
    else:
        $ hermione_custom_outfit = True
        
        call h_update_hair
        
        if hermione_custom_outfit_list[0][custom_outfit] != "":
            $ hermione_custom_a = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[0][custom_outfit]
        else:
            $ hermione_custom_a = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
        
        if hermione_custom_outfit_list[1][custom_outfit] != "":
            $ hermione_custom_b = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[1][custom_outfit]
        else:
            $ hermione_custom_b = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
        
        if hermione_custom_outfit_list[2][custom_outfit] != "":
            $ hermione_custom_c = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[2][custom_outfit]
        else:
            $ hermione_custom_c = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
        
        if hermione_custom_outfit_list[3][custom_outfit] != "":
            $ hermione_custom_d = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[3][custom_outfit]
        else:
            $ hermione_custom_d = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
            
        if hermione_custom_outfit_list[4][custom_outfit] != "":
            $ hermione_custom_e = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[4][custom_outfit]
        else:
            $ hermione_custom_e = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
        
        $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/"+str(hermione_custom_outfit_breast_list[custom_outfit])+".png"
    return
    
    
## Action Blocks
label set_hermione_action(action = ""):
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with d3
    call h_action(action)
    return
    
label h_action(action =  ""):
    $ hermione_action = False
    $ h_action_show_arms = False
    $ h_action_show_top = True
    $ h_action_show_skirt = True
    $ h_action_show_bra = True
    
    $ override = False
    
    if hermione_wear_panties or h_request_wear_panties or whoring < h_stop_wearing_panties_lvl:
        $ h_action_show_panties = True
    else:
        $ h_action_show_panties = False
    if hermione_wear_bra:
        $ h_action_show_bra = True
    else:
        $ h_action_show_bra = False
    
    $ h_action_a = "00_blank.png"
    $ h_action_b = "00_blank.png"
    $ h_action_left_arm = "clothes/uniform/action/00_blank.png"
    $ h_action_right_arm = "clothes/uniform/action/00_blank.png"
    call update_her_uniform
    
    if action == "" or action == "none" or action == 0:
        pass
    else:
        if hermione_custom_outfit:
            if action == "lift_skirt":
                pass
            if action == "lift_top":
                if custom_outfit == 2 or custom_outfit == 3:
                    $ h_action_a = "cherr_flash.png"
                if custom_outfit == 7:
                    $ h_action_a = "power_costume_2.png"
        else:
            $ hermione_action = True
            $ hermiome_action_bra = hermione_bra
            $ hermiome_action_panties = hermione_panties
            $ hermiome_action_top = hermione_top
            $ hermiome_action_skirt = hermione_skirt
            
            if action == "lift_skirt":
                $ h_action_show_skirt = False
                $ h_action_show_arms = True
                if whoring <= 5:
                    $ h_action_a = "lift_skirt_1.png"
                if whoring >= 6 and whoring <= 11:
                    $ h_action_a = "lift_skirt_2.png"
                if whoring >= 12 and whoring <= 19:
                    $ h_action_a = "lift_skirt_3.png"
                if whoring >= 20:
                    $ h_action_a = "lift_skirt_4.png"
                $ h_action_left_arm = "clothes/uniform/action/lift_skirt_fix.png"
                
            if action == "lift_top":
                $ h_action_show_top = False
                $ h_action_show_bra = False
                if whoring <= 3:# shirt_00
                    $ h_action_a = "lift_top_1.png"
                elif whoring >= 4 and whoring <= 20:
                    $ h_action_a = "lift_top_2-4.png"
                elif whoring >= 21:
                    if day_random <= 4:# shirt_04
                        $ h_action_a = "lift_top_5_3.png"
                    if day_random >= 5:# shirt_05
                        $ h_action_a = "lift_top_6.png"
                if hermione_perm_expand:
                    $ h_action_b = "lift_top_expand_perm_overlay.png"
                else:
                    $ h_action_b = "lift_top_normal_overlay.png"
            
            if action == "hold_book":
                $ h_action_show_top = False
                if whoring <= 3:# shirt_00
                    $ h_action_a = "hold_book_1.png"
                elif whoring >= 4 and whoring <= 7:# shirt_01
                    $ h_action_a = "hold_book_2.png"
                elif whoring >= 8 and whoring <= 14:# shirt_02
                    $ h_action_a = "hold_book_3.png"
                elif whoring >= 15 and whoring <= 20:# shirt_03
                    $ h_action_a = "hold_book_4.png"
                elif whoring >= 21:
                    if day_random <= 4:# shirt_04
                        $ h_action_a = "hold_book_5.png"
                    if day_random >= 5:# shirt_05
                        $ h_action_a = "hold_book_6.png"
            
            if action == "expand_breasts" or action == "expand_all":
                $ h_action_show_top = False
                $ h_action_show_bra = False
                $ h_action_show_arms = True
                $ h_action_left_arm = "body/arms/left/left_1.png"
                $ h_action_right_arm = "body/arms/right/right_1.png"
                $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded.png" 
            
            if action == "expand_ass" or action == "expand_all":
                $ h_action_show_skirt = False
                $ h_action_show_panties = False
                $ h_action_show_arms = True
                $ h_action_left_arm = "body/arms/left/left_1.png"
                $ h_action_right_arm = "body/arms/right/right_1.png"
                if whoring >= h_stop_wearing_panties_lvl:
                    $ hermione_legs = "01_hp/13_characters/hermione/body/legs/expanded_ass.png"
                else:
                    $ hermione_legs = "01_hp/13_characters/hermione/body/legs/expanded_ass_panties.png"
            
            if action == "lift_breasts":
                $ h_action_show_top = False
                $ h_action_show_bra = False
                $ h_action_a = "lift_breasts.png"
                $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_normal.png" 
                
            if action == "lift_breasts_large":
                $ h_action_show_top = False
                $ h_action_show_bra = False
                $ h_action_a = "lift_breasts_large.png"
                $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_nipfix.png" 
                
            if action == "hands_behind":
                $ h_action_show_top = False
                $ h_action_show_skirt = False
                $ h_action_show_arms = True
                $ override = True
                $ hermiome_action_a = "01_hp/13_characters/hermione/body/arms/left/behind.png"
                $ hermione_action_right_arm = "01_hp/13_characters/hermione/body/arms/right/hand_behind.png"
                #$ h_action_left_arm = "body/arms/left/behind.png"
                #$ h_action_right_arm = "body/arms/right/hand_behind.png"
                
            if action == "hands_cuffed":
                $ h_action_show_top = False
                $ h_action_show_arms = True
                $ h_action_left_arm = "body/arms/left/cuffed.png"
                
            if action == "hands_free":
                $ h_action_show_arms = True
                $ h_action_left_arm = "body/arms/left/left_1.png"
                $ h_action_right_arm = "body/arms/right/right_1.png"
    
    if not override:
        $ hermione_action_right_arm = "01_hp/13_characters/hermione/"+str(h_action_right_arm)
        $ hermione_action_left_arm = "01_hp/13_characters/hermione/"+(h_action_left_arm)
        $ hermiome_action_a = "01_hp/13_characters/hermione/clothes/uniform/action/"+str(h_action_a)
        $ hermiome_action_b = "01_hp/13_characters/hermione/clothes/uniform/action/"+str(h_action_b)
        $ hermione_custom_action_a = "01_hp/13_characters/hermione/clothes/custom/"+str(h_action_a)
    
    if action == "hold_book":
        $ hermiome_action_b = hermione_hair_b
    if action == "lift_skirt" and (h_top >= 2 and h_top <= 4):
        $ hermiome_action_top = "01_hp/13_characters/hermione/clothes/uniform/action/lift_skirt_top_"+str(h_top)+".png"
    
    if hermione_wetpanties == True and action == "lift_skirt" and hermione_wear_panties == True:
        $ hermiome_action_b = "01_hp/13_characters/hermione/overlays/pantystain.png"
        
    return
    
    
## Control Blocks
label h_update:
    $ hermione_body = "01_hp/13_hermione_main/"+str(h_body)+".png"
    #$ hermione_body = "01_hp/13_characters/hermione/body/face/"+str(h_body)+".png"
    
    if h_tears != "":
        $ hermione_tears = "01_hp/13_characters/hermione/body/face/tears/"+str(h_tears)+".png"
    else:
        $ hermione_tears = "01_hp/13_characters/hermione/body/face/tears/00_blank.png"
    
    if h_body in hermione_anger or hermione_emote_anger:
        $ hermione_emote = "01_hp/13_characters/emote/01.png"
    elif h_body in hermione_exclam or hermione_emote_exclam:
        $ hermione_emote = "01_hp/13_characters/emote/02.png"
    elif h_body in hermione_hearts or hermione_emote_hearts:
        $ hermione_emote = "01_hp/13_characters/emote/03.png"
    elif h_body in hermione_question or hermione_emote_question:
        $ hermione_emote = "01_hp/13_characters/emote/04.png"
    elif h_body in hermione_sweat or hermione_emote_sweat:
        $ hermione_emote = "01_hp/13_characters/emote/05.png"
    elif hermione_body in hermione_suprize or hermione_emote_suprize:
        $ hermione_emote = "01_hp/13_characters/emote/06.png"
    else:
        $ hermione_emote = "01_hp/13_characters/emote/00_blank.png"
    return
   
label h_update_body:
    if not hermione_wear_top:
        if not hermione_wear_bra:
            if not hermione_perm_expand:
                $ h_breasts = "breasts_normal" # normal breasts
            else:
                $ h_breasts = "breasts_expanded" # expanded breasts
        elif h_bra in h_bra_nip_fix:
            $ h_breasts = "breasts_normal" # normal breasts
        else:
            $ h_breasts = "breasts_nipfix" # nipple corrected breasts
    else:
        $ h_breasts = "breasts_nipfix"
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/"+str(h_breasts)+".png"
    $ hermione_legs = "01_hp/13_characters/hermione/body/legs/legs_1.png"
    return
    
label h_update_hair:
    if hermione_custom_outfit and hermione_custom_outfit_hair_list[custom_outfit] != "":
        $ hermione_hair_a = "01_hp/13_characters/hermione/clothes/custom/"+str(hermione_custom_outfit_hair_list[custom_outfit])+".png"
        $ hermione_hair_b = "01_hp/13_characters/hermione/clothes/custom/"+str(hermione_custom_outfit_hair_list[custom_outfit])+"_2.png"
    else:
        $ hermione_hair_a = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+".png"
        $ hermione_hair_b = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+"_2.png"
    return
    
label update_her_uniform:
    call h_update_body
    call h_update_hair
    call update_chibi_uniform
    
    ### TOP
    if whoring <= 3:# top 1
        $ h_top = "top_1"
    elif whoring >= 4 and whoring <= 7:# top 2
        $ h_top = "top_2"
    elif whoring >= 8 and whoring <= 14:# top 3
        $ h_top = "top_3"
    elif whoring >= 15 and whoring <= 20:# top 4
        $ h_top = "top_4"
    elif whoring >= 21:
        if day_random <= 4:# top 5
            $ h_top = "top_5"
        if day_random >= 5:# top 6
            $ h_top = "top_6"
    
    ### SKIRT
    if whoring <= 5 and h_skirt == "base_skirt": # skirt 1
        $ h_skirt = "skirt_1"
    if whoring >= 6 and whoring <= 11 and h_skirt == "base_skirt": # skirt 2
        $ h_skirt = "skirt_2"
    if whoring >= 12 and whoring <= 19 and h_skirt == "base_skirt": # skirt 3
        $ h_skirt = "skirt_3"
    if whoring >= 20 and h_skirt == "base_skirt": # skirt 4
        $ h_skirt = "skirt_4"
        
        
    ### PANTIES
    if whoring >= h_stop_wearing_panties_lvl:
        $ hermione_wear_panties = False
    if hermione_wetpanties:
        $ hermione_panties_overlay = "01_hp/13_characters/hermione/overlays/pantystain.png"
    else:
        $ hermione_panties_overlay = "01_hp/13_characters/hermione/overlays/00_blank.png"
        
    
    $ hermione_bra = "01_hp/13_characters/hermione/clothes/underwear/"+str(h_bra)+".png"
    $ hermione_stockings = "01_hp/13_characters/hermione/clothes/stockings/"+str(h_stocking)+".png"
    $ hermione_panties = "01_hp/13_characters/hermione/clothes/underwear/"+str(h_panties)+".png"
    $ hermione_skirt = "01_hp/13_characters/hermione/clothes/uniform/"+str(h_skirt)+".png"
    $ hermione_badge = "01_hp/13_characters/hermione/clothes/badges/"+str(h_badge)+".png"
    $ hermione_top = "01_hp/13_characters/hermione/clothes/uniform/"+str(h_top)+".png"
    
    if custom_skirt == 1: # jeans
        $ hermione_skirt = "01_hp/23_clothes_store/existing_stock/jeans.png"
        
    if custom_skirt == 5: # short_jeans
        $ hermione_skirt = "01_hp/23_clothes_store/existing_stock/jeans_short.png"
    
    return
    
label update_chibi_uniform:
    
    if not wear_shirts:
        $ hermione_chibi_blink = "ch_hem blink_n"
        $ hermione_chibi_blink_f = "ch_hem blink_n_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_n_01.png"
        $ hermione_chibi_walk = "ch_hem walk_n"
        $ hermione_chibi_walk_f = "ch_hem walk_n_flip"
    elif whoring <= 3:# shirt_00
        $ hermione_chibi_blink = "ch_hem blink_a"
        $ hermione_chibi_blink_f = "ch_hem blink_a_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_a_01.png"
        $ hermione_chibi_walk = "ch_hem walk_a"
        $ hermione_chibi_walk_f = "ch_hem walk_a_flip"
    elif whoring >= 4 and whoring <= 7:# shirt_01
        $ hermione_chibi_blink = "ch_hem blink_d"
        $ hermione_chibi_blink_f = "ch_hem blink_d_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_d_01.png"
        $ hermione_chibi_walk = "ch_hem walk_d"
        $ hermione_chibi_walk_f = "ch_hem walk_d_flip"
    elif whoring >= 8 and whoring <= 14:# shirt_02
        $ hermione_chibi_blink = "ch_hem blink_e"
        $ hermione_chibi_blink_f = "ch_hem blink_e_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_e_01.png"
        $ hermione_chibi_walk = "ch_hem walk_e"
        $ hermione_chibi_walk_f = "ch_hem walk_e_flip"
    elif whoring >= 15 and whoring <= 20:# shirt_03
        $ hermione_chibi_blink = "ch_hem blink_f"
        $ hermione_chibi_blink_f = "ch_hem blink_f_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_f_01.png"
        $ hermione_chibi_walk = "ch_hem walk_f"
        $ hermione_chibi_walk_f = "ch_hem walk_f_flip"
    elif whoring >= 21:
        if day_random <= 4:# shirt_04
            $ hermione_chibi_blink = "ch_hem blink_g"
            $ hermione_chibi_blink_f = "ch_hem blink_g_flip"
            $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_g_01.png"
            $ hermione_chibi_walk = "ch_hem walk_g"
            $ hermione_chibi_walk_f = "ch_hem walk_g_flip"
        if day_random >= 5:# shirt_05
            $ hermione_chibi_blink = "ch_hem blink_h"
            $ hermione_chibi_blink_f = "ch_hem blink_h_flip"
            $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_h_01.png"
            $ hermione_chibi_walk = "ch_hem walk_h"
            $ hermione_chibi_walk_f = "ch_hem walk_h_flip"
        
    return
    
label reset_hermione_main:
    show screen hermione_blank_main
    show screen hermione_blank_head
    show screen hermione_blank_chibi
    hide screen hermione_blank_main
    hide screen hermione_blank_head
    hide screen hermione_blank_chibi
    
    $ aftersperm = False #Show cum stains on Hermione's uniform.
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with d3
    call h_outfit(0)
    call h_action("none")
    call update_her_uniform
    return
     
     
label set_custom_layer(a=hermione_custom_a,b=hermione_custom_b,c=hermione_custom_c,d=hermione_custom_d,e=hermione_custom_e,breast=h_breasts, save = False):
    if a != hermione_custom_a:
        $ hermione_custom_a = a
    if b != hermione_custom_b:
        $ hermione_custom_b = b
    if c != hermione_custom_c:
        $ hermione_custom_c = c
    if d != hermione_custom_d:
        $ hermione_custom_d = d
    if e != hermione_custom_e:
        $ hermione_custom_e = e
        
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/"+str(breast)+".png"
    
    if save:
        call h_save_custom_outfit
    return
    
     
label h_load_custom_outfit(outfit_id=-1):
    if outfit_id != -1:
        $ hermione_custom_outfit = True
        $ hermione_custom_a = hermione_custom_outfit_list[0][outfit_id]
        $ hermione_custom_b = hermione_custom_outfit_list[1][outfit_id]
        $ hermione_custom_c = hermione_custom_outfit_list[2][outfit_id]
        $ hermione_custom_d = hermione_custom_outfit_list[3][outfit_id]
        $ hermione_custom_e = hermione_custom_outfit_list[4][outfit_id]
    return
        
label h_save_custom_outfit(hair = "", breastType = "breasts_1"):
    
    $ outfit_name = ""
    $ outfit_name = renpy.input("(Use keyboard to enter the a name fot thid Outfit.)")
    $ outfit_name = outfit_name.strip()
    if outfit_name == "":
        $ hermione_outfit_names.append("Outfit_"+str(len(hermione_custom_outfit_hair_list)))
    else:
        $ hermione_outfit_names.append(outfit_name)
    
    $ hermione_custom_outfit_list[0].append(hermione_custom_a)
    $ hermione_custom_outfit_list[1].append(hermione_custom_b)
    $ hermione_custom_outfit_list[2].append(hermione_custom_c)
    $ hermione_custom_outfit_list[3].append(hermione_custom_d)
    $ hermione_custom_outfit_list[4].append(hermione_custom_e)
    
    $ hermione_custom_outfit_hair_list.append(hair)
    $ hermione_custom_outfit_breast_list.append(breastType)
    $ hermione_outfit_id.append("user_created_outfit_"+str(h_player_generated_outfits))
        
    $ h_player_generated_outfits += 1
    return
    
label new_main_menu: # testing menu found in cheats or jumped to
    show screen hermione_main
    menu:
        "-update main-":
            call update_her_uniform
            jump new_main_menu
        "-robes-":
            menu:
                "-off-":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/00_blank.png"
                    $ hermione_wear_robe = False
                    jump new_main_menu
                "-gryff robe basic-":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe gap-":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe_gap.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe wide gap":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe_gap_wide.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe off":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe_off.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe no shirt":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe_shirt_none.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe quidditch":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_quidditch.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
        "-outfits-":
            label new_main_menu_outfit:
            menu:
                "-action-":
                    menu:
                        "-none-":
                            call h_action("")
                            jump new_main_menu_outfit
                        "-lift top-":
                            call h_action("lift_top")
                            jump new_main_menu_outfit
                        "-back-":
                            jump new_main_menu_outfit
                "-No Outfit-":
                    call h_outfit(0)
                    jump new_main_menu_outfit
                "-Defined Outfits-":
                    label new_main_menu_outfit_defined:
                    call set_defined_menu_vars
                    $ choice = renpy.display_menu(h_menu_list)
                    if choice == -1:
                        jump new_main_menu_outfit
                    else:
                        call h_outfit(choice)
                        jump new_main_menu_outfit_defined
                "-make your own-":
                    menu make_your_own:
                        "-create outfit-":
                            $ hermione_custom_a = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
                            $ hermione_custom_b = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
                            $ hermione_custom_c = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
                            $ hermione_custom_d = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
                            $ hermione_custom_e = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
                            $ hermione_custom_action_a = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
                            $ hermione_custom_outfit = True
                            menu make_your_own_create:
                                "-save current state-":
                                    call h_save_custom_outfit
                                    jump make_your_own
                                "-top-":
                                    menu make_your_own_top:
                                        "-jumper-":
                                            call set_custom_layer(c="01_hp/13_characters/hermione/clothes/custom/mix-match/jumper.png")
                                            jump make_your_own_top
                                        "-white t-":
                                            call set_custom_layer(c="01_hp/13_characters/hermione/clothes/custom/mix-match/white_t.png")
                                            jump make_your_own_top
                                        "-back-":
                                            jump make_your_own_create
                                "-bottom-":
                                    menu make_your_own_bottom:
                                        "-Long Jeans-":
                                            call set_custom_layer(b="01_hp/13_characters/hermione/clothes/custom/mix-match/jeans_long.png")
                                            jump make_your_own_bottom
                                        "-Short Jeans-":
                                            call set_custom_layer(b="01_hp/13_characters/hermione/clothes/custom/mix-match/jeans_short.png")
                                            jump make_your_own_bottom
                                        "-Skirt A-":
                                            call set_custom_layer(b="01_hp/13_characters/hermione/clothes/custom/mix-match/skirt_2.0.png")
                                            jump make_your_own_bottom
                                        "-Skirt B-":
                                            call set_custom_layer(b="01_hp/13_characters/hermione/clothes/custom/mix-match/skirt_3.0.png")
                                            jump make_your_own_bottom
                                        "-back-":
                                            jump make_your_own_create
                                "-breasts-":
                                    menu make_your_own_breasts:
                                        "-nipple fix-":
                                            call set_custom_layer(breast="breasts_1")
                                            jump make_your_own_breasts
                                        "-no nipples-":
                                            call set_custom_layer(breast="breasts_2.5")
                                            jump make_your_own_breasts
                                        "-normal-":
                                            call set_custom_layer(breast="breasts_2")
                                            jump make_your_own_breasts
                                        "-back-":
                                            jump make_your_own_create
                                "-back-":
                                    jump make_your_own
                        "-view outfit-":
                            call set_custom_menu_vars
                            $ choice = renpy.display_menu(h_menu_list)
                            if choice == -1:
                                jump new_main_menu_outfit
                            else:
                                call h_load_custom_outfit(choice)
                                jump new_main_menu_outfit
                        "-Back-":
                            jump new_main_menu_outfit
                "-Back-":
                    jump new_main_menu
        
        "-hair-":
            label new_main_menu_hair:
            menu:
                "-Hair A-":
                    $ h_hair_style = "A"
                    call update_her_uniform
                    jump new_main_menu_hair
                "-Hair B-":
                    $ h_hair_style= "B"
                    call update_her_uniform
                    jump new_main_menu_hair
                "-Color-":
                    menu:
                        "-Brown-":
                            $ h_hair_color = 1
                            call update_her_uniform
                            jump new_main_menu_hair
                        "-Blonde-":
                            $ h_hair_color = 2
                            call update_her_uniform
                            jump new_main_menu_hair
                        "-Red-":
                            $ h_hair_color = 3
                            call update_her_uniform
                            jump new_main_menu_hair
                        "-Black-":
                            $ h_hair_color = 4
                            call update_her_uniform
                            jump new_main_menu_hair
                        "-Blue-":
                            $ h_hair_color = 5
                            call update_her_uniform
                            jump new_main_menu_hair
                        "-Orange-":
                            $ h_hair_color = 6
                            call update_her_uniform
                            jump new_main_menu_hair
                "-Back-":
                    jump new_main_menu
        
        "-Actions-":
            label new_main_menu_actions:
            menu:
                "-Lift top-":
                    call h_action("lift_top")
                    jump new_main_menu_actions
                "-Lift Skirt-":
                    call h_action("lift_skirt")
                    jump new_main_menu_actions
                "-Hold Book-":
                    call h_action("hold_book")
                    jump new_main_menu_actions
                "-Expand All-":
                    call h_action("expand_all")
                    jump new_main_menu_actions
                "-Expand Breasts-":
                    call h_action("expand_breasts")
                    jump new_main_menu_actions
                "-Expand Ass-":
                    call h_action("expand_ass")
                    jump new_main_menu_actions
                "-Lift Breasts-":
                    call h_action("lift_breasts")
                    jump new_main_menu_actions
                "-Lift Breasts Large-":
                    call h_action("lift_breasts_large")
                    jump new_main_menu_actions
                "-Arms Behind-":
                    call h_action("hands_behind")
                    jump new_main_menu_actions
                "-Arms cuffed-":
                    call h_action("hands_cuffed")
                    jump new_main_menu_actions
                "-No Action-":
                    call h_action("")
                    jump new_main_menu_actions
                "-Back-":
                    jump new_main_menu
        
        "-Base clothes-":
            label new_main_menu_base_clothes:
            menu:
                "-Toggle Top-":
                    if hermione_wear_top:
                        $ hermione_wear_top = False
                    else:
                        $ hermione_wear_top = True
                    call update_her_uniform
                    jump new_main_menu_base_clothes
                "-Toggle Bra-":
                    if hermione_wear_bra:
                        $ hermione_wear_bra = False
                    else:
                        $ hermione_wear_bra = True
                    call update_her_uniform
                    jump new_main_menu_base_clothes
                "-Toggle Skirt-":
                    if hermione_wear_skirt:
                        $ hermione_wear_skirt = False
                    else:
                        $ hermione_wear_skirt = True
                    call update_her_uniform
                    jump new_main_menu_base_clothes
                "-Toggle Panties-":
                    if hermione_wear_panties:
                        $ hermione_wear_panties = False
                    else:
                        $ hermione_wear_panties = True
                    call update_her_uniform
                    jump new_main_menu_base_clothes
                    
                    
                "-Back-":
                    jump new_main_menu
        
        "-Underwear-":
            label new_main_menu_underwear:
            menu:
                "-normal-":
                    $ h_bra = "base_bra_white_1"
                    $ h_panties = "base_panties_1"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-cup-":
                    $ h_bra = "cup_bra"
                    $ h_panties = "cup_panties"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-lace-":
                    $ h_bra = "lace_bra"
                    $ h_panties = "lace_panties"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-silk-":
                    $ h_bra = "silk_bra"
                    $ h_panties = "silk_panties"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-latex-":
                    $ h_bra = "latex_bra"
                    $ h_panties = "latex_panties"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-Back-":
                    jump new_main_menu
        
        "-Stockings-":
            label new_main_menu_stocking:
            menu:
                "-none-":
                    $ h_stocking = "00_blank"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-black-":
                    $ h_stocking = "black"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-fishnet_a-":
                    $ h_stocking = "fishnet_a"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-fishnet_b-":
                    $ h_stocking = "fishnet_b"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-gryff-":
                    $ h_stocking = "gryff"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-gryff_vibe-":
                    $ h_stocking = "gryff_vibe"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-lace-":
                    $ h_stocking = "lace"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-latex-":
                    $ h_stocking = "latex"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-slyth_vibe-":
                    $ h_stocking = "slyth_vibe"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-white-":
                    $ h_stocking = "white"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-pantyhose grey-":
                    $ h_stocking = "pantyhose grey"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-pantyhose tan-":
                    $ h_stocking = "pantyhose tan"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-Back-":
                    jump new_main_menu
        
        "-Toggle perm expand-":
            if hermione_perm_expand:
                $ hermione_perm_expand = False
            else:
                $ hermione_perm_expand = True
            call update_her_uniform
            jump new_main_menu            
            
        "-Hide Menu-":
            show screen ctc
            pause
            jump new_main_menu
        
        "-Never mind-":
            hide screen hermione_main
            jump day_main_menu
    
label set_h_animation(ani=u_h_animation, xpos = u_h_ani_xpos, ypos = u_h_ani_ypos):
    if ani != u_h_animation:
        $ u_h_animation = ani
    if ani == "sex_ani":
        $ u_h_ani_xpos = -210
        $ u_h_ani_ypos = 10
    if ani == "blowjob_ani":
        $ u_h_animation_paused = "hand_ani"
        $ u_h_ani_xpos = -150
        $ u_h_ani_ypos = 10
    return

label play_h_animation:
    hide screen u_h_ani_scr_pause
    if u_h_animation == "sex_ani":
        hide screen genie
        show screen chair_02
    if ani == "blowjob_ani":
        hide screen genie
        show screen chair_02
    #if:
    
    show screen u_h_animation
    return
    
label pause_u_animation:
    hide screen u_h_ani_scr
    show screen u_h_ani_scr_pause
    with d2
    return
    
label end_h_animation:
    if u_h_animation == "sex_ani":
        show screen genie
        hide screen chair_02
        hide screen u_h_animation
    #if:
    return
    
label set_defined_menu_vars:
    python:
        tmp_list_a = []
        tmp_list_b = []
        for i in range(0,hermione_defined_outfit_list_size):
            if hermione_outfit_names[i] not in ["null",""]:
                tmp_list_a.append(hermione_outfit_names[i])
                tmp_list_b.append(i)
        
        h_menu_list = [[0 for i in xrange(2)] for i in xrange(len(tmp_list_a)+1)]
        for i in range(0,len(tmp_list_a)):
            h_menu_list[i][0] = tmp_list_a[i]
            h_menu_list[i][1] = tmp_list_b[i]
        h_menu_list[len(h_menu_list)-1][0] = "-nevermind-"
        h_menu_list[len(h_menu_list)-1][1] = -1
    return
    
    
label set_custom_menu_vars:
    python:
        tmp_list_a = []
        tmp_list_b = []
        for i in range(hermione_defined_outfit_list_size,len(hermione_outfit_names)):
            if hermione_outfit_names[i] not in ["null",""]:
                tmp_list_a.append(hermione_outfit_names[i])
                tmp_list_b.append(i)
        
        h_menu_list = [[0 for i in xrange(2)] for i in xrange(len(tmp_list_a)+1)]
        for i in range(0,len(tmp_list_a)):
            h_menu_list[i][0] = tmp_list_a[i]
            h_menu_list[i][1] = tmp_list_b[i]
        h_menu_list[len(h_menu_list)-1][0] = "-nevermind-"
        h_menu_list[len(h_menu_list)-1][1] = -1
    return
    
screen u_h_ani_scr:
    add u_h_animation at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)
    
screen u_h_ani_scr_pause:
    add u_h_animation_paused at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)
    
init python:
    
    
    def changeHermione( hair_color=None,
                        hair_style=None,
                        face=None,
                        
                        x_pos=None,
                        y_pos=None):
        ###DEFINE GLOBAL VARIABLES
        global h_xpos
        global h_ypos
        global h_base
        global h_body
        global h_hair_color
        global h_hair_style
        ###HIDE OLD SCREEN
        renpy.hide_screen("hermione_main_new")
        renpy.with_statement(Dissolve(0.5))
        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            h_xpos = x_pos
        else:
            h_xpos = luna_xpos
        if y_pos is not None:
            h_ypos = y_pos
        else:
            h_ypos = h_ypos
        
        
        if hair_color is not None and (hair_color >= 1 and hair_color <= 6):
            h_hair_color = hair_color
        else:
            h_hair_color = h_hair_color
            
        if hair_style is not None and (hair_style == "A" or hair_style == "B"):
            h_hair_style = hair_style
        else:
            h_hair_style = h_hair_style
        
        hermione_hair_a = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+".png"
        hermione_hair_b = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+"_2.png"
        
        if face is not None:
            h_body = h_body
    
    
    
    def changeHermioneDialoug(   image_name,
                                    hid_char_list=None,
                                    hid_dialog_list=None,
                                    x_pos=370,
                                    y_pos=0,
                                    hide_trans=Dissolve(0.3),
                                    show_trans=Dissolve(0.3),
                                    char_list=None,
                                    dialog_list=None):
        # SCOPE THESE VARIABLES TO GLOBAL SO WE CAN REALLY
        # UPDATE THEM
        global h_xpos
        global h_ypos
        global h_body
        renpy.hide_screen("hermione_main")
        if hide_trans is not None:
            renpy.with_statement(hide_trans)
        #dialog if present
        if hid_char_list is not None:
            if len(hid_char_list) == 1:
                #single character
                for i in range(0,len(hid_dialog_list)):
                    renpy.say(hid_char_list[0],hid_dialog_list[i])
            elif len(hid_char_list) > 1:
                #multiple characters
                for i in range(0,len(hid_char_list)):
                    renpy.say(hid_char_list[i],hid_dialog_list[i])
        h_xpos = x_pos
        h_ypos = y_pos
        if image_name is not None:
            h_body = image_name

        renpy.show_screen("hermione_main")
        if show_trans is not None:
            renpy.with_statement(show_trans)
        #dialog if present
        if char_list is not None:
            if len(char_list) == 1:
                #single character
                for i in range(0,len(dialog_list)):
                    renpy.say(char_list[0],dialog_list[i])
            elif len(char_list) > 1:
                #multiple characters
                for i in range(0,len(char_list)):
                    renpy.say(char_list[i],dialog_list[i])
                   