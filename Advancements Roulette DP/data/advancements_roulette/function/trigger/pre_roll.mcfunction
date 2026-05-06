scoreboard players reset @s adv.roll
scoreboard players enable @s adv.roll
execute if score @s adv.roll.cooldown matches 1.. run return run function advancements_roulette:messages/cooldown
execute if score @s adv.roll.cooldown matches 0 run return run function advancements_roulette:trigger/roll with storage advancements_roulette:advancements_roulette