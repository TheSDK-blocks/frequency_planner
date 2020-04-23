add wave -position insertpoint  \
sim/:tb_frequency_planner:A \
sim/:tb_frequency_planner:initdone \
sim/:tb_frequency_planner:clock \
sim/:tb_frequency_planner:Z \

run -all
