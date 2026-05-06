title @s title [{translate:"advancements_roulette:roll.title",fallback:"And you rolled a %1$s!",with:[{storage:"advancements_roulette:advancements_roulette",nbt:"rolled",color:"light_purple"}]}]
$title @s subtitle [{translate:"chat.square_brackets",fallback:"[%1$s]",color:"green",with:[{storage:"advancements_roulette:advancements_roulette",nbt:"display.[$(rolled)].\"title\"",interpret:true}]}]
tellraw @s [{translate:"advancements_roulette:roll.chat.border",color:"#449944"}]
tellraw @s ""
$tellraw @s [{translate:"chat.square_brackets",fallback:"[%1$s]",color:"#66ff66",with:[{storage:"advancements_roulette:advancements_roulette",nbt:"display.[$(rolled)].\"title\"",interpret:true,hover_event:{action:"show_text",value:[{storage:"advancements_roulette:advancements_roulette",nbt:"display.[$(rolled)].\"title\"",interpret:true,color:"#66ff66"},"\n",{storage:"advancements_roulette:advancements_roulette",nbt:"display.[$(rolled)].\"desc\"",interpret:true}]}}]}]
$tellraw @s [{text:" "},{storage:"advancements_roulette:advancements_roulette",nbt:"display.[$(rolled)].\"desc\"",interpret:true}]
tellraw @s ""
tellraw @s [{translate:"advancements_roulette:roll.chat.border",color:"#449944"}]