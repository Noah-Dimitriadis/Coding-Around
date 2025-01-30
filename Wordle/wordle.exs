# wordle pattern matching for next available words for next guess
# TODO double letter handling
defmodule Solver do
  @words File.read!("WordBank.txt")
  |> String.split("\n", trim: true)

  def get_words, do: @words

  def get_input do
    input = IO.gets("Enter your last guess in the form !a?b%c where ! = green, ? = yellow, % = grey: ")
    |> String.trim()
    |> String.downcase()
    if valid_input(input) do
      input
    else
      IO.puts("Invalid input. Please try again.")
      get_input()
    end
  end

  defp valid_input(input) do
    if String.length(input) == 10 and Regex.match?(~r/^([!?%][a-z]{1})+$/, input)do
      true
    else
      false
    end
  end

  def suggest_words(pattern) do
    grey_letters = extract_grey_chars(pattern)
    yellow_letters = extract_yellow_chars(pattern)
    green_letters = extract_green_chars(pattern)
    @words |> Enum.filter(fn word -> eligible_words?(word, grey_letters, yellow_letters, green_letters) end)
    # |> check positions of green letters
    # |> check positions of yellow letters
  end

  defp eligible_words?(word, grey_letters, yellow_letters, green_letters) do
    word_chars = String.graphemes(word)   # split into char list

    has_grey = Enum.all?(word_chars, fn char -> char in grey_letters end)
    has_yellow = Enum.all?(yellow_letters, fn char -> char in word_chars end)
    has_green = Enum.all?(green_letters, fn char -> char in word_chars end)

    has_yellow and has_green and not has_grey
  end

  defp check_green_pos(word, pattern) do
    word_chars = String.graphemes(word)
    pattern
    |> String.to_charlist()
    |> Enum.chunk_every(2)
    |> Enum.filter(fn [symbol, _] -> symbol == ?! end)
    # |> Enum.map(fn [index, char] -> ) maybe something like this??
    # find position indexes of green letters
    # if index of char in word_chars == green char and == green char index return true
  end

  defp check_yellow_pos(word, pattern) do
    # word to charlist
    # find position indexes of green letters
    # if index of char in word_chars == yellow char and != yellow char index return true
  end

  defp extract_grey_chars(pattern) do
    pattern
    |> String.to_charlist()
    |> Enum.chunk_every(2)
    |> Enum.filter(fn [symbol, _] -> symbol == ?% end)
    |> Enum.map(fn [_, letter] -> <<letter>> end)
  end

  defp extract_yellow_chars(pattern) do
    pattern
    |> String.to_charlist()
    |> Enum.chunk_every(2)
    |> Enum.filter(fn [symbol, _] -> symbol == ?? end)
    |> Enum.map(fn [_, letter] -> <<letter>> end)
  end

  defp extract_green_chars(pattern) do
    pattern
    |> String.to_charlist()
    |> Enum.chunk_every(2)
    |> Enum.filter(fn [symbol, _] -> symbol == ?! end)
    |> Enum.map(fn [_, letter] -> <<letter>> end)
  end

  def run do
    input = get_input()
    valid_words = suggest_words(input)
    IO.inspect(valid_words)
  end
end

Solver.run()

# %f?r?e%s%h
# %f%r%e?s?h
# %f%r%e%s?h
