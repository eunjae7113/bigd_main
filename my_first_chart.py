import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"   #윈도우는Malgun Gothic
weight = [63, 73, 71, 70, 68]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(weight)
for i, p in enumerate(weight):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
        xytext=(0, 8), ha="center")
    
ax.set_title("내 몸무게 변화")
fig.savefig("my_first_chart.png")