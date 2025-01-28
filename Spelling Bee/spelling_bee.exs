# attempt to solve nyt spelling bee game using Elixir pattern matching

defmodule M do
  def f(arg) do
    "transformed #{arg}"
  end

end
[arg1] = System.argv
IO.puts M.f(arg1)
