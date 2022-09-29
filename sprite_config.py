from EZSprite import SimpleSprite, MultiSprite

# Enter Coords
shop_scene_loc = [-719, -550]
test_scene_loc = [-370, -90]
outside_scene_loc = [-439, -330]

# Bounds
shop_scene_bounds = [30, 31, 37, 38, 39, 40, 45, 63, 103, 146, 147, 156, 162, 163, 172,
                     188, 259, 260, 319, 349, 350, 351, 414, 430, 672, 688, 710, 726,
                     727, 742, 743, 758, 759, 774, 775, 1174, 1190, 1522, 1538]
shop_scene_ibounds = [0, 1]

test_scene_bounds = [42, 45, 63, 102, 103, 105, 1296, 1298, 1306, 1307, 1312, 1314, 1322, 1323, 1372, 1373, 1388, 1389]
test_scene_ibounds = [1]

outside_bounds = [70, 80, 89, 98, 103, 108, 118, 119, 120, 121, 289, 290, 291, 310, 294, 313, 332, 333, 334, 335, 336, 317, 298, 424, 443, 462, 464, 465, 446, 427, 266, 267]
outside_ibounds = [0, 1]

# CSV
shop_scene_floor = "Assets/CSV/shop_floor.csv"
shop_scene_wall = "Assets/CSV/shop_wall.csv"
shop_scene_dec_base = "Assets/CSV/shop_dec_base.csv"
shop_scene_dec_overlay = "Assets/CSV/shop_dec_overlay.csv"
shop_scene_collide_dec = "Assets/CSV/shop_collide_dec.csv"
shop_scene_interact = "Assets/CSV/shop_interact.csv"

test_scene_floor = "Assets/CSV/test_floor.csv"
test_scene_wall = "Assets/CSV/test_wall.csv"
test_scene_dec = "Assets/CSV/test_dec.csv"
test_scene_interact = "Assets/CSV/test_interact.csv"

outside_floor = "Assets/CSV/outside_floor.csv"
outside_homes = "Assets/CSV/outside_homes.csv"
outside_collide = "Assets/CSV/outside_collide.csv"
outside_interact = "Assets/CSV/outside_interact.csv"

# SimpleSprite
shop_scene_visual = SimpleSprite("Assets/PNG/shop_sheet.png", 16, 2)
shop_scene_visual.addIgnoreCSV(shop_scene_floor)
shop_scene_visual.addCSV(shop_scene_wall)
shop_scene_visual2 = SimpleSprite("Assets/PNG/shop_dec_sheet.png", 16, 2)
shop_scene_visual2.addCSV(shop_scene_collide_dec)
shop_scene_visual2.addIgnoreCSV(shop_scene_dec_base)
shop_scene_visual2.addIgnoreCSV(shop_scene_dec_overlay)
shop_scene_interaction = SimpleSprite("Assets/PNG/interact.png", 16, 2)
shop_scene_interaction.addCSV(shop_scene_interact)

test_scene_visual = SimpleSprite("Assets/PNG/shop_sheet.png", 16, 2)
test_scene_visual.addIgnoreCSV(test_scene_floor)
test_scene_visual.addCSV(test_scene_wall)
test_scene_visual2 = SimpleSprite("Assets/PNG/shop_dec_sheet.png", 16, 2)
test_scene_visual2.addCSV(test_scene_dec)
test_scene_interaction = SimpleSprite("Assets/PNG/interact.png", 16, 2)
test_scene_interaction.addCSV(test_scene_interact)

outside_visual = SimpleSprite("Assets/PNG/village_sheet.png", 16, 2)
outside_visual.addIgnoreCSV(outside_floor)
outside_visual.addIgnoreCSV(outside_homes)
outside_visual.addCSV(outside_collide)
outside_interaction = SimpleSprite("Assets/PNG/village_sheet.png", 16, 2)
outside_interaction.addCSV(outside_interact)

# MultiSprite
shop_scene = MultiSprite("shop")
shop_scene.addSimpleSprite(shop_scene_visual)
shop_scene.addSimpleSprite(shop_scene_visual2)
shop_scene.addInteractive(shop_scene_interaction)
shop_scene.defineSceneBounds(shop_scene_bounds)
shop_scene.defineSceneiBounds(shop_scene_ibounds)

test_scene = MultiSprite("test")
test_scene.addSimpleSprite(test_scene_visual)
test_scene.addSimpleSprite(test_scene_visual2)
test_scene.addInteractive(test_scene_interaction)
test_scene.defineSceneBounds(test_scene_bounds)
test_scene.defineSceneiBounds(test_scene_ibounds)

outside_scene = MultiSprite("outside")
outside_scene.addSimpleSprite(outside_visual)
outside_scene.addInteractive(outside_interaction)
outside_scene.defineSceneBounds(outside_bounds)
outside_scene.defineSceneiBounds(outside_ibounds)
