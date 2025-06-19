def recommend_cards(user_input, cards):
    filtered = []
    for card in cards:
        income_required = parse_income_requirement(card.get('eligibility', ''))
        if user_input['income'] >= income_required:
            score = 0
            # Check benefit match
            card_perks_lower = [perk.lower() for perk in card['perks']]
            match_count = sum(1 for benefit in user_input['benefits'] if benefit.lower() in card_perks_lower)
            score += match_count * 2  # Give more weight to matched benefits
            # Reward score
            score += card['reward_rate'] * user_input['spend'] * 12
            filtered.append((card, score))
    return sorted(filtered, key=lambda x: x[1], reverse=True)[:5]
