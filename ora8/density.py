volume_lead = 18
volume_copper = 23
density_lead = 11.34
density_copper = 8.69

weight_lead = volume_lead * density_lead
weight_copper = volume_copper * density_copper

print("olom nehezebb mint a rez:", weight_lead > weight_copper)
