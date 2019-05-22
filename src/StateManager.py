import tkinter as tk
from src.FileManager import DataType
from src.lib import clamp

class StateManager:
  def __init__(self, data: DataType, rows: int, columns: int, pixel_on_hex_color: str, pixel_off_hex_color: str):
    self.current_page = tk.IntVar()
    self.current_page.set(0)
    self.data = data
    self.rows = rows
    self.columns = columns
    self.pixel_on_hex_color = pixel_on_hex_color
    self.pixel_off_hex_color = pixel_off_hex_color

  def set_pixel_buttons(self, buttons) -> None:
    self.buttons = buttons
    self.goto_valid_page(self.current_page.get())

  def goto_valid_page(self, page: int) -> None:
    page = clamp(page, 0, len(self.data) // self.rows - 1)
    self.current_page.set(page)
    for i in range(0, self.rows):
      for j in range(0, self.columns):
        color = self.pixel_off_hex_color if self.data[self.rows * page + i][j] == 0 else self.pixel_on_hex_color
        self.buttons[i][j].config(highlightbackground=color)

  def handle_page_change(self, count: int, is_relative: bool = True):
    def wrapper():
      page = count + (self.current_page.get() if is_relative else 0)
      self.goto_valid_page(page)
    return wrapper

  def handle_pixel_click(self, i: int, j: int):
    def wrapper():
      self.on_pixel_click(i, j)
    return wrapper
  
  def on_pixel_click(self, i: int, j: int) -> None:
    di = self.rows * self.current_page.get() + i
    self.data[di][j] += 1 if self.data[di][j] == 0 else -1
    color = self.pixel_off_hex_color if self.data[di][j] == 0 else self.pixel_on_hex_color
    self.buttons[i][j].config(highlightbackground=color)

  def on_add_empty_frame_before(self) -> None:
    self.insert_frame(self.create_empty_frame())

  def on_add_empty_frame_after(self) -> None:
    self.insert_frame(self.create_empty_frame(), 1)

  def on_duplicate_frame_before(self) -> None:
    self.insert_frame(self.duplicate_current_frame())

  def on_duplicate_frame_after(self) -> None:
    self.insert_frame(self.duplicate_current_frame(), 1)

  def on_clear_frame(self) -> None:
    index = self.rows * self.current_page.get()
    self.data[index:(index+self.rows)] = self.create_empty_frame()
    self.goto_valid_page(self.current_page.get())

  def on_remove_frame(self) -> None:
    if (self.current_page.get() == 0) and (len(self.data) <= self.rows):
      return
    index = self.rows * self.current_page.get()
    del self.data[index:(index+self.rows)]
    self.goto_valid_page(self.current_page.get())

  def insert_frame(self, frame, offset: int = 0) -> None:
    new_page_number = self.current_page.get() + offset
    index = self.rows * new_page_number
    self.data[index:index] = frame
    self.goto_valid_page(new_page_number)

  def create_empty_frame(self):
    new_frame = []
    for _ in range(0, self.rows):
      new_frame.append([0] * self.columns)
    return new_frame

  def duplicate_current_frame(self):
    index = self.rows * self.current_page.get()
    return [[e for e in r] for r in self.data[index:(index+self.rows)]]
