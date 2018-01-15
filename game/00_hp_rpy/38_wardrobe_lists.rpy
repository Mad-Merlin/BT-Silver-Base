

label update_wardrobe_lists:

### Hair Color ###
#    $ wr_her_haircolor = ["dye_1"]







### Tops ###
    $ wr_her_tops = ["1"] #Page MAX=25

    if whoring >= 3: #get right number
        $ wr_her_tops.append("2")
    if whoring >= 6: #get right number
        $ wr_her_tops.append("3")
    if whoring >= 9: #get right number
        $ wr_her_tops.append("4")
    if whoring >= 12: #get right number
        $ wr_her_tops.append("5")
    if whoring >= 18: #get right number
        $ wr_her_tops.append("6")


### Bottoms ###
    $ wr_her_bottoms = ["skirt_1"] #Page MAX=25

    ## Skirts ##
    if whoring >= 3: #get right number
        $ wr_her_bottoms.append("skirt_2")
    if whoring >= 6: #get right number
        $ wr_her_bottoms.append("skirt_3")
    if whoring >= 9: #get right number
        $ wr_her_bottoms.append("skirt_4")
    if whoring >= 12: #get right number
        $ wr_her_bottoms.append("skirt_5")
    #if micro_skirt unlocked/purchased:
    #    $ wr_her_bottoms.append("skirt_6") #micro skirt
    #ADD japan_pant

    ## Jeans ##
    if "jeans_long" in cs_existing_stock:
        $ wr_her_bottoms.append("jeans_long")
    if "jeans_short" in cs_existing_stock:
        $ wr_her_bottoms.append("jeans_short")
    #ADD rocker_skirt


### Stockings ###

    $ wr_her_stockings_wool = [] #10 total

    if "gryff_stockings" in cs_existing_stock:
        $ wr_her_stockings_wool.append("gryff_stockings")
    if "gryff_stockings_vibe" in cs_existing_stock:
        $ wr_her_stockings_wool.append("gryff_stockings_vibe")
    if "gryff_cheer_stockings_short" in cs_existing_stock:
        $ wr_her_stockings_wool.append("gryff_cheer_stockings_short")
    if "gryff_cheer_stockings" in cs_existing_stock:
        $ wr_her_stockings_wool.append("gryff_cheer_stockings")
    if "gryff_cheer_stockings_vibe" in cs_existing_stock:
        $ wr_her_stockings_wool.append("gryff_cheer_stockings_vibe")

    if "slyth_stockings" in cs_existing_stock:
        $ wr_her_stockings_wool.append("slyth_stockings")
    if "slyth_stockings_vibe" in cs_existing_stock:
        $ wr_her_stockings_wool.append("slyth_stockings_vibe")
    if "slyth_cheer_stockings_short" in cs_existing_stock:
        $ wr_her_stockings_wool.append("slyth_cheer_stockings_short")
    if "slyth_cheer_stockings" in cs_existing_stock:
        $ wr_her_stockings_wool.append("slyth_cheer_stockings")
    if "slyth_cheer_stockings_vibe" in cs_existing_stock:
        $ wr_her_stockings_wool.append("slyth_cheer_stockings_vibe")
    #ADD Ravenclaw Blue. And maybe Hufflepuff.


    $ wr_her_stockings_lace = []

    if "lace_stockings" in cs_existing_stock:
        $ wr_her_stockings_lace.append("lace_stockings")

    $ wr_her_stockings_wicked = []

    if "fishnet_stockings" in cs_existing_stock:
        $ wr_her_stockings_wicked.append("fishnet_stockings")

    #Pantyhose
    $ wr_her_pantyhose = []

    #Gloves
    $ wr_her_gloves = []


### Robes ###
    $ wr_her_robes = ["gryff_robe","gryff_robe_off"]
    if whoring >= 3:
        $ wr_her_robes.append("gryff_robe_shirt_none")
    if whoring >= 6:
        $ wr_her_robes.append("gryff_robe_gap_wide")
    if whoring >= 9:
        $ wr_her_robes.append("gryff_quidditch")


    if whoring >= 6:
        $ wr_her_robes.append("slyth_robe")
        $ wr_her_robes.append("slyth_robe_off")
        $ wr_her_robes.append("slyth_robe_shirt_none")
    if whoring >= 9:
        $ wr_her_robes.append("slyth_robe_gap_wide")
    if whoring >= 12:
        $ wr_her_robes.append("slyth_quidditch")




    return
