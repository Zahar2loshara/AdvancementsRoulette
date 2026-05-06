scoreboard players set @s adv.roll.cooldown 200
$execute store result storage advancements_roulette:advancements_roulette rolled int 1 run random roll 0..$(how_many_there_are)
execute store result score @s adv.current_advancement run data get storage advancements_roulette:advancements_roulette rolled
function advancements_roulette:messages/roll with storage advancements_roulette:advancements_roulette