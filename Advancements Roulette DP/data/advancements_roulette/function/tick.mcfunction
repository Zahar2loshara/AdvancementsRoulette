execute as @a if score @s adv.roll matches 1.. run function advancements_roulette:trigger/pre_roll
execute as @a if score @s adv.settings matches 1.. run function advancements_roulette:trigger/settings
execute as @a if score @s adv.roll.cooldown matches 1.. run scoreboard players remove @s adv.roll.cooldown 1
schedule function advancements_roulette:tick 1t replace