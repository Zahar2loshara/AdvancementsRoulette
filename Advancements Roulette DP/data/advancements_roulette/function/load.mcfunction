schedule clear advancements_roulette:messages/no_command_storage
execute unless data storage advancements_roulette:advancements_roulette display run function advancements_roulette:messages/no_command_storage
execute store result storage advancements_roulette:advancements_roulette how_many_there_are int 1 run data get storage advancements_roulette:advancements_roulette display
function advancements_roulette:tick

scoreboard objectives add adv.roll trigger
scoreboard players enable @e adv.roll
scoreboard objectives add adv.settings trigger
scoreboard players enable @e adv.settings
scoreboard objectives add adv.current_advancement dummy
scoreboard objectives add adv.roll.cooldown dummy {translate:"advancements_roulette:adv.roll.cooldown",fallback:"cooldown for rerolling"}