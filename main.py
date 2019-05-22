import sys
import tkinter as tk
from typing import List
from src.load import config
from src.FileManager import FileManager
from src.StateManager import StateManager

if __name__ == '__main__':
  filename = sys.argv[1]
  fm = FileManager(filename, config['rows'], config['columns'])
  fm.read()
  if (fm.is_data_corrupt()):
    decision = input('data file is corrupt, fix it automatically? (y/n): ')
    if (decision == 'y' or decision == 'Y'):
      fm.fix_data()
    else:
      sys.exit()
  fm.write()

  app = tk.Tk()
  sm = StateManager(fm.data, fm.rows, fm.columns, config['pixel_on_hex_color'], config['pixel_off_hex_color'])

  header_section = tk.Frame(app)
  tk.Button(header_section, text='Remove Current Frame', command=sm.on_remove_frame, highlightbackground=config['remove_current_frame_color']).pack(side=tk.LEFT)
  tk.Button(header_section, text='Clear Current Frame', command=sm.on_clear_frame, highlightbackground=config['clear_current_frame_color']).pack(side=tk.LEFT)
  tk.Button(header_section, text='Add Empty Frame', command=sm.on_add_frame, highlightbackground=config['add_empty_frame_color']).pack(side=tk.RIGHT)
  tk.Button(header_section, text='Add Copy Of Current Frame', command=sm.on_duplicate_frame, highlightbackground=config['add_duplicate_frame_color']).pack(side=tk.RIGHT)
  tk.Button(header_section, text='Save', command=fm.write, highlightbackground=config['save_button_color']).pack()
  header_section.pack()

  buttons = []
  matrix_section = tk.Frame(app)
  for i in range(0, fm.rows):
    row_of_buttons = []
    for j in range(0, fm.columns):
      frame = tk.Frame(matrix_section, width=config['pixel_size'], height=config['pixel_size'])
      button = tk.Button(frame, command=sm.handle_pixel_click(i, j))
      button.grid(sticky="wens")
      frame.grid_propagate(False) #disables resizing of frame
      frame.columnconfigure(0, weight=1) #enables button to fill frame
      frame.rowconfigure(0,weight=1) #any positive number would do the trick
      frame.grid(row=i, column=j) #put frame where the button should be
      row_of_buttons.append(button)
    buttons.append(row_of_buttons)
  matrix_section.pack()
  sm.set_pixel_buttons(buttons)

  footer_section = tk.Frame(app)
  for i, nav_size in enumerate(sorted(config['nav_sizes'], reverse=True)):
    button_color = config['contrast_dark'] if (i % 2 == 0) else config['contrast_light']
    tk.Button(footer_section, text='-{0}'.format(nav_size), command=sm.handle_page_change(-nav_size), highlightbackground=button_color).pack(side=tk.LEFT)
    tk.Button(footer_section, text='+{0}'.format(nav_size), command=sm.handle_page_change(nav_size), highlightbackground=button_color).pack(side=tk.RIGHT)
  tk.Label(footer_section, textvariable=sm.current_page).pack(side=tk.BOTTOM)
  footer_section.pack()

  app.mainloop()
