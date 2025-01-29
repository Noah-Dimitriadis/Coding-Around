# wordle pattern matching for next best guess

defmodule Solver do
  @words File.read!("WordBank.txt")
  |> String.split("\n", trim: true)

  def get_words, do: @words

  defp valid_input(input) do
    if String.length(input) == 10 and Regex.match?(~r/^([!?%][a-z]{1})+$/, input)do
      true
    else
      false
    end
  end

  def get_input do
    input = IO.gets("Enter your last guess: ")
    |> String.trim()
    |> String.downcase()
    if valid_input(input) do
      IO.puts("#{input} is valid!")
      input
    else
      IO.puts("Invalid input, please enter 5 letters")
      get_input()
    end
  end

  def match(input) do
    words = get_words()
    if Enum.member?(words, input) do
      IO.puts("true")
    else
      IO.puts("false")
    end
  end

  def suggest_words(pattern) do
    guessed_letters = extract_guessed_chars(pattern)
    @words |> Enum.filter(fn word -> match_word?(word, pattern, guessed_letters) end)
  end

  def match_word? do

  end

  def extract_guessed_chars(pattern) do
    pattern |> String.to_charlist()
    |> Enum.chunk_every(2)
  end

  def run do
    get_input()
    |> match
  end
end

Solver.run()
