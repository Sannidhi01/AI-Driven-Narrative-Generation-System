def build_act_specification(character_data, world_config, act_name):
    return {
        "act": act_name,
        "world_description": world_config["description"],
        "governance": world_config["governance"],
        "core_conflicts": world_config["conflicts"],
        "advisor_role": world_config["advisor_role"],
        "factions": character_data["factions"],
        "advisor": character_data["advisor"],
        "themes": character_data["themes"],
        "constraints": [
            "Explain how decisions are made and enforced in the system",
            "Highlight the moments where the automated choices create problems",
            "Show how different groups experience same decisions differently",
            "End the act by reflecting the long term impacts of these choices",
            "Avoid direct phrases and references from original story"
        ]
    }

