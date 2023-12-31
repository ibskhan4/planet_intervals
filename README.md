# Planet Intervals Problem

A spaceship is approaching some planets that are arranged in a 1-dimensional line. It needs to pass through the line of the planets, but can't get too close to any planet, otherwise it would get caught in that planet's gravitational field.

Given a list of planets, where each planet is specified by its position along the line and the range of its gravitational field, compute the list of gaps from [0, 1000] through which the spaceship can fly.

| Input                | Output                    | Reasoning                                        |
|----------------------|---------------------------|--------------------------------------------------|
| [3,2]                | [0,1],[5,1000]            | The field covers [1,5].                          |
| [3,2],[5,1]          | [0,1],[6,1000]            | The fields cover [1,5] and [4,6].                |
| [2,1],[5,1]          | [0,1],[3,4],[6,1000]      | The fields cover [1,3] and [4,6].                |
| [2,2],[7,1],[4,1]    | [5,6],[8,1000]            | The fields cover [0,4], [6,8], and [3,5].        |

