---
marp: true
theme: uncover
class: invert
color: #ccc
style: |
  .columns {
    display: flex;
    justify-content: center;
  }
math: mathjax
---

## Мультиагентоное планирование с неполной информацией

<span style="color: grey">Выполнил:</span> Матюхин Григорий

---

1. Задача
1. Понятие "Планирование"
1. Математическая точка зрения
1. Алгоритмы
1. Надежность и полнота 

---

## Кооперативное распределенное уточнительное планировани

---

## Ограничения

- Агенты независимы друг от друга
- Агенты знают не все о своей среде или их знания не верны
- Агенты имеют приватные и публичные знания
- Агент может предложить план
- Другие агенты могут внести уточнения
- Итоговый план выбирается сообща

---

Planning

Multi-agent plannig 

---

- $\mathcal{O}$ -- objects
- $\mathcal{V}$ -- state variables
- $\mathcal{D}_v$ -- objects of the planning domain

---

$$
\langle v, d\rangle 
$$
$$
\langle v,\neg d\rangle 
$$
$$
(v, d)
$$

$$
\DeclareMathOperator{\pre}{pre}
\DeclareMathOperator{\eff}{eff}
\langle \pre(a), \eff(a)\rangle
$$

---

## MAP task

$$
\Large\mathcal{T} = \langle \mathcal{AG}, \mathcal{V}, \mathcal{A}, \mathcal{I}, \mathcal{G} \rangle
$$

---

## В общих чертах

1. Агент составляет изначальный план используя только свои знания
1. Агент делится частью своих знаний с другими агентами
1. Агент составляет распределенный план
1. Агент предлагает уточнения к плану
1. Все агенты соглашаются на одном из планов и выполняют его

---

## Распределенный план

```python
while received_fluents:
    for f in received_fluents:
        if f not in RPG_i:
            RPG_i.add(f)
            RPG_i_cost[f] = cost(f)
        if f in RPG_i and cost(f) > RPG_i_cost:
            RPG_i_cost[f] = cost(f)
# ...
# ommited: RPG expansion
```

---

## Уточнение

```python
while True:
    goal = open_goals[base_plan]
    plan = plans[goal]

    send_to_others(refinements[plan])
    other_refinements = get_from_others(plan)
    refinements += other_refinements

    for p in refinements[plan]:
        evals[plan][p] = eval_plan(p)

    best_plan = evals.select_best()
    base_plan = best_plan
    
    if open_goals(base_plan).empty():
        return base_plan
```

---

## Надежность и полнота

---

## Спасибо за внимание
