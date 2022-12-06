import matplotlib.pyplot as plt
import numpy as np


### SETUP
data = [["123 \n 123 \n 123", "345", "567", "789"],
        ["12", "34", "56", "78"],
        [1, 2, 3, 4]]

column_headers = ["Simple", "Complex", "Iris", "Seeds"]
row_headers = ["random", "plusplus", "kaufman"]


title_text = 'Test Results'
footer_text = 'Month Day, 2022'
#fig_background_color = 'skyblue'
#fig_border = 'steelblue'


# Create the figure. Setting a small pad on tight_layout
# seems to better regulate white space. Sometimes experimenting
# with an explicit figsize here can produce better outcome.
plt.figure(linewidth=2,
           tight_layout={'pad':1},
           #figsize=(5,3)
          )

# Add a table at the bottom of the axes
the_table = plt.table(cellText=data,
                      rowLabels=row_headers,
                      #rowColours=rcolors,
                      rowLoc='right',
                      #colColours=ccolors,
                      colLabels=column_headers,
                      loc='center')


# Scaling is the only influence we have over top and bottom cell padding.
# Make the rows taller (i.e., make cell y scale larger).
the_table.scale(1, 4)

# Hide axes
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# Hide axes border
plt.box(on=None)

# Add title
plt.suptitle(title_text)

# Add footer
plt.figtext(0.95, 0.05, footer_text, horizontalalignment='right', size=6, weight='light')
# Force the figure to update, so backends center objects correctly within the figure.
# Without plt.draw() here, the title will center on the axes and not the figure.
plt.draw()

plt.show()