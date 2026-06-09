import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st

def engine(dfs, type_plot, x_axis=None, y_axis=None, use_formatter=False, unit='%', **arg):
  # Definición de paleta profesional y configuración global
  color2 = ["#003f5c", "#2f4b7c", "#665191", "#a05195", "#d45087", "#f95d6a", "#ff7c43", "#ffa600"]
  sns.set_palette(sns.color_palette(color2))
  
  # iterating the dictionary
  for name, df in dfs.items():
    try:
      # define what to iterate
      if isinstance(y_axis, list):
        col_list = y_axis
      elif isinstance(x_axis, list):
        col_list = x_axis
      else:
        col_list = [x_axis] if x_axis else [y_axis]

      # setting plot dimension
      n_vars = len(col_list)
      cols = 1 if n_vars == 1 else 2
      rows = math.ceil(n_vars / cols)
      
      
      if type_plot == 'pie':
        fig_width = 15 if cols == 1 else 22
        fig_height = 8.5 * rows
      else:
        fig_width = 15 if cols == 1 else 22
        fig_height = 12 * rows
        
      fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(fig_width, fig_height))

      # flattening the axes
      axes = axes.flatten() if n_vars > 1 else [axes]

      for i, col in enumerate(col_list):
        current_ax = axes[i]

        # dynamic axis assignment
        if isinstance(x_axis, list):
          actual_x, actual_y = col, y_axis
        elif isinstance(y_axis, list):
          actual_x, actual_y = x_axis, col
        else:
          actual_x = x_axis if x_axis else col
          actual_y = y_axis

        # plot section
        if type_plot == 'count':
          sns.countplot(data=df,
                        x=actual_x,
                        ax=current_ax,
                        **arg
                        )

          current_ax.tick_params(axis='x', rotation=90, labelsize=15)
          current_ax.tick_params(axis='y', labelsize=15)

          for container in current_ax.containers:
            current_ax.bar_label(container, fontsize=15, padding=3)

        elif type_plot == 'bar':
          sns.barplot(data=df,
                      x=actual_x,
                      y=actual_y,
                      ax=current_ax,
                      **arg
                      )

          current_ax.tick_params(axis='x', labelsize=15)
          current_ax.tick_params(axis='y', labelsize=15)

          for container in current_ax.containers:
            val_unit = '$' if unit == '$' else ('%' if unit == '%' else '')
            labels = [f'{val_unit}{x:,.2f}' if val_unit == '$' else f'{x:,.2f}{val_unit}' for x in container.datavalues]
            current_ax.bar_label(container, labels=labels, padding=4, fontsize=15)

        elif type_plot == 'box':
          sns.boxplot(data=df,
                      x=actual_x,
                      y=actual_y,
                      ax=current_ax,
                      **arg
                      )

          current_ax.tick_params(axis='x', rotation=90, labelsize=15)
          current_ax.tick_params(axis='y', labelsize=15)

        elif type_plot == 'violin':
          sns.violinplot(
              data=df,
              x=actual_x,
              y=actual_y,
              ax=current_ax,
              **arg
              )
          current_ax.tick_params(labelsize=15)
        
        elif type_plot == 'pie':
          labels_pie = df[actual_x].tolist()
          values_pie = df[actual_y].tolist()
          
          # Aplicamos la paleta configurada globalmente
          current_palette = sns.color_palette(n_colors=len(values_pie))
          
          wedges, texts, autotexts = current_ax.pie(
              values_pie, 
              labels=labels_pie, 
              autopct='%1.1f%%', 
              startangle=90,
              colors=current_palette
          )
          
          for t in texts:
              t.set_fontsize(16)
          for at in autotexts:
              at.set_fontsize(15)
              
          current_ax.axis('equal')

        elif type_plot == 'scatter':
          sns.scatterplot(
            data=df,
            x=actual_x,
            y=actual_y,
            ax=current_ax,
            **arg
          )

          plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, fontsize=14)
          current_ax.tick_params(labelsize=15)

        if use_formatter:
          current_ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

        # Títulos grandes y negritas
        current_ax.set_title(f"{type_plot.upper()} PLOT OF {name}", fontsize=24, weight='bold', pad=15)
        current_ax.grid(axis='x', linestyle='--', alpha=0.6)
        
        current_ax.xaxis.label.set_size(16)
        current_ax.yaxis.label.set_size(16)

      for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

      plt.tight_layout(pad=3.0)
      
      st.pyplot(fig)
      plt.close(fig)

    except AttributeError:
      print(f"ERROR: Object '{name}' is not a valid pandas DataFrame and cannot be plotted.\n")
      plt.close()

    except Exception as e:
      print(f"ERROR: Failed to generate plots for DataFrame '{name}'. Technical details: {e}\n")
      plt.close()