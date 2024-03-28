<!-- TODO: add headings to all slides, remove slides with section headings -->
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

## Мультиагентное планирование с неполной информацией

<span style="color: grey">Выполнил:</span> Матюхин Григорий

---

1. Задача
1. Определения
1. Алгоритм
1. Надежность и полнота 

---

## Задача

- Агенты независимы друг от друга
- Агенты знают не все о своей среде или их знания не верны
- Агенты имеют приватные и публичные знания
- Агент может предложить план
- Другие агенты могут внести уточнения
- Итоговый план выбирается сообща

---

<!--  WARN: bad -->
## Мультиагентное планирование

---

- $\mathcal{O}$ &mdash; объекты
- $\mathcal{V}$ &mdash; переменные состояния
- $\mathcal{D}_v$ &mdash; значения переменных, $\mathcal{D}_v \subseteq \mathcal{O}$

---

Состояние: $S = \left\{ \langle v_1, d_1\rangle, \langle v_2, \neg d_2\rangle, \ldots, \langle v_n, d_n\rangle \right\}$

<div style="width: 1px; height: 3rem;"></div>

$(v_n, d_n) =$ Истина, если $\langle v_n, d_n \rangle \in S$ 
$(v_n, d_n) =$ Ложь, если $\langle v_n, \neg d_n \rangle \in S$

---

Информация о $\langle v, d \rangle$ для агента $i$:

- **Полная**: $v \in \mathcal{V}_i, d \in \mathcal{D}_{v_i}$
- **Частичная**: $v \in \mathcal{V}_i, d \notin \mathcal{D}_{v_i}$,
    агент видит $\langle v, \bot\rangle$
- **Нет**: $v \notin \mathcal{V}_i, d \notin \mathcal{D}_{v_i}$

---

Действие: $
\DeclareMathOperator{\pre}{pre}
\DeclareMathOperator{\eff}{eff}
a = \langle \pre(a), \eff(a)\rangle
$

<div style="width: 1px; height: 3rem;"></div>

$$ \pre(a) = \left\lbrace (v_i, d_i), \neg (v_j, d_j), \ldots \right\rbrace$$

$$ \eff(a) = \left\lbrace \langle v_i, \neg d_i\rangle, \langle v_j, d_j\rangle, \ldots \right\rbrace$$

---

Задача мультиагентного планирования:

<div style="width: 1px; height: 3rem;"></div>

$$
\Large\mathcal{T} = \langle \mathcal{AG}, \mathcal{V}, \mathcal{A}, \mathcal{I}, \mathcal{G} \rangle
$$

---

## Описание алгоритма

<!-- WARN: too much text -->

1. Агент составляет изначальный план используя только свои знания
1. Агент делится частью своих знаний с другими агентами
1. Агент составляет распределенный план
1. Агент предлагает уточнения к плану
1. Все агенты соглашаются на одном из планов и выполняют его

---

### Распределенный план

```python
# ommited: share and receive fluents with other agents
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

<!--  WARN: bad -->
### Уточнение плана

```python
while True:
    goal = open_goals[base_plan]
    plan = plans[goal]

    # ommited: share and receive refinements with other agents

    for p in refinements[plan]:
        evals[plan][p] = eval_plan(p)

    base_plan = evals.select_best()
    if open_goals(base_plan).empty():
        return base_plan
```

---

## Правильность алгоритма

---

Пусть существует план $\prod$ где:
$\langle v,d_1\rangle \in \prod$.

<div style="width: 1px; height: 3rem;"></div>

Пусть существует уточнение $\prod'$ где:
один из эффектов: $(v = d_2)$

<div style="width: 1px; height: 3rem;"></div>

$(v = d_2)$ &mdash; угроза $\prod$

---

В зависимости от информации о $v$:

- **Полная**: несоответствие обнаружено
- **Частичная**: агент видит $\langle v, \bot\rangle$, $\bot \neq d_1$
- **Нет**: действие не может быть выполнено

---

## Полнота алгоритма

---

## Вывод

---

## Спасибо за внимание
