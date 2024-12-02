import matplotlib.pyplot as plt

states = ["Madhya Pradesh", "Rajasthan"]
mp_results = {"BJP": 163, "INC": 66, "BSP": 0, "Others": 1}
rj_results = {"INC": 69, "BJP": 115, "BSP": 2, "Others": 13}

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

state_results = [mp_results, rj_results]

for i, (state, results) in enumerate(zip(states, state_results)):
    parties = list(results.keys())
    seats = list(results.values())
    total_seats = sum(seats)
    percentages = [seat / total_seats * 100 for seat in seats]
    explode = [0.1 if p == max(percentages) else 0 for p in percentages]
    axes[i].pie(
        seats, labels=[f"{p} ({s})" for p, s in zip(parties, seats)],
        autopct=lambda p: f'{p:.1f}%', explode=explode, startangle=90
    )
    axes[i].set_title(f"Seat Share: {state}")

fig, ax = plt.subplots(figsize=(10, 6))

party_names = list(mp_results.keys())
mp_seats = list(mp_results.values())
rj_seats = [rj_results[party] for party in party_names]
x = range(len(party_names))
bar_width = 0.4

ax.bar(x, mp_seats, width=bar_width, label="Madhya Pradesh", color='blue', alpha=0.7)
ax.bar([p + bar_width for p in x], rj_seats, width=bar_width, label="Rajasthan", color='orange', alpha=0.7)

ax.set_xticks([p + bar_width / 2 for p in x])
ax.set_xticklabels(party_names)
ax.set_ylabel("Seats Won")
ax.set_title("Party-wise Seat Share in Madhya Pradesh and Rajasthan")
ax.legend()

plt.tight_layout()
plt.show()
