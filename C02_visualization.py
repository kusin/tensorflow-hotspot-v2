# lib visualizations data
import matplotlib.pyplot as plt
# --------------------------------------------------------------

# visualisasi timeseries plot
def lineplot1(x, y, label, title):

  # membuat time series plot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(x, y, color="tab:blue", label=label, linewidth=2.5)

  # membuat label-label
  ax.set_title(title, fontsize=12)
  ax.set_xlabel("", fontsize=12)
  ax.set_ylabel("", fontsize=12)
  ax.legend(loc="best")
  ax.grid(True)

  # return values
  return plt.show()
# --------------------------------------------------------------


# visualisasi timeseries plot
def lineplot2(x1, y1, label1, x2, y2, label2, title):

  # membuat time series plot
  fig, ax = plt.subplots(figsize = (8,4))
  ax.plot(x1, y1, color="tab:blue", label=label1, linewidth=2.5)
  ax.plot(x2, y2, color="tab:red", label=label2, linewidth=2.5)

  # membuat label-label
  ax.set_title(title, fontsize=12)
  ax.set_xlabel("", fontsize=12)
  ax.set_ylabel("", fontsize=12)
  ax.legend(loc="best")
  ax.grid(True)

  # return values
  return plt.show()
# --------------------------------------------------------------