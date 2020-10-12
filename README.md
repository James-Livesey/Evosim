# Evosim
An evolution simulator written in Python. Oh dear.

## Running Evosim
To run Evosim, you'll need Python 3 installed. Then, you'll want to run the main
program using:

```shell
python3 main.py
```
(Or equivalent for your platform.)

## Concepts
* **World**: The place in which inhabitants reside.
* **Tick**: A unit of time; time advances by a tick when you press the Enter key
  in the shell.
* **Inhabitant**: An organism which exists in the world. Inhabitants can either
  reproduce or die.
* **Decay**: A type of death by old age (predetermined by their `decay` value
  at birth).
* **Property**: An effect which inhabitants have and may pass onto future
  generations of inhabitants. Similar to how genes work IRL. Properties can
  define abstract information, such as eye colour, but also info such as gender
  (which is used by Evosim to match parents for reproduction).
* **Dominant property**: A property that takes precedent over its less-dominant
  counterpart in a pair.
* **Condition**: A type of property which could cause an inhabitant to die.
* **Reproduction**: Ermmm... go ask your parents!
* **Fertility**: The maximum number of times that an inhabitant can reproduce.
  This value goes down for a particular inhabitant every time they reproduce,
  and when an inhabitant is born, a random fertility value between 0 and 5
  inclusive is given to them.
* **Label**: The name given to a thing, such as an inhabitant, property or
  condition.
* **Property adoption**: Where an inhabitant has a property (but it doesn't
  necessarily mean that the inhabitant expresses that property).
* **Property expression**: Where an inhabitant adopts a property and can be
  affected by that property (by, for example, conditions).

## Commands
* **(Pressing Enter)**: Advance the world's clock by 1 tick.
* **`exit`**: Exit Evosim.
* **`help`**: Display this readme.
* **`repeat`**: Repeat a command.
    - `Command to repeat?`: Command to repeatedly execute. Press `#` to cancel.
    - `Number of times to repeat command?`: Number of times to repeat the
      command.
* **`new property`**: Create a new property.
    - `New property's label?`: The label to give to the property.
    - `Is property dominant?`: Whether the property is dominant.
* **`list properties`**: List created properties.
* **`new inhabitant`**: Create a new inhabitant and place it in the world.
    - `New inhabitant's label?`: The label to give to the inhabitant.
    - `First property label in property pair?`: The first property to assign to
      the inhabitant in a new property pair. Inhabitants can have multiple
      property pairs, and property pairs can contain two of the same property.
    - `Second property label in property pair?`: The second property to assign
      to the inhabitant in a new property pair.
* **`new inhabitant batch`**: Create a specified amount of new inhabitants and
  place them into the world.
    - `First property label in property pair?`: The first property to assign to
      the inhabitant in a new property pair. Inhabitants can have multiple
      property pairs, and property pairs can contain two of the same property.
    - `Second property label in property pair?`: The second property to assign
      to the inhabitant in a new property pair.
    - `Number of inhabitants to create?`: The number of inhabitants to create
      and place into the world.
* **`list inhabitants`**: List the inhabitants that are currently alive.
* **`inspect inhabitant`**: View the properties and values of a particular
  inhabitant.
    - `Label of inhabitant to inspect?`: The label of the inhabitant to inspect.
* **`new condition`**: Create a new condition to bind to a property.
    - `New condition's label?`: The label to give to the condition.
    - `Affecting property's label?`: The label of the property to bind the
      condition to. When an inhabitant expresses this property, they will have
      the condition.
    - `Decay length?`: The time (in ticks) for which the inhabitant will have to
      live until the condition kills them.
* **`list conditions`**: List all conditions.
* **`calculate property adoption`**: View the number of inhabitants that
  adopt/express the specified property.
    - `Property label to use in calculation?`: The label of the property to use
      to calculate its adoption.
* **`export inhabitant history to json`**: Export the world's inhabitant history
  to JSON for use in external programs.
    - `Filename to export to?`: The name of the file to export the JSON data to.
      This will be in the `exports` folder.
* **`graph inhabitant history`**: Generate a text-based graph of inhabitant
  history and save it to a file.
    - `Filename to graph to?` The name of the file to export the graph to. This
      will be in the `graphs` folder.
    - `Width condensation of graph data?`: The number of inhabitants per
      character in the X axis of the graph.