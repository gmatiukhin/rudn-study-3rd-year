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

## Содержание

1. Задача
1. Определения
1. Алгоритм
1. Надежность и полнота 

---

## Задача

Разработать подход кооперативного планирования, который позволит агентам работать с неполной информацией о мире.

---

## Ограничения

- Агенты независимы друг от друга
- Агенты знают не все о своей среде или их знания не верны
- Агенты имеют приватные и публичные знания
- Агент может предложить план
- Другие агенты могут внести уточнения
- Итоговый план выбирается сообща

---

## Модель мультиагентного планирования

---

## Домен

- $\mathcal{O}$ &mdash; объекты
- $\mathcal{V}$ &mdash; переменные состояния
- $\mathcal{D}_v$ &mdash; значения переменных, $\mathcal{D}_v \subseteq \mathcal{O}$

---

## Знания агента о мире

Состояние: $S = \left\{ \langle v_1, d_1\rangle, \langle v_2, \neg d_2\rangle, \ldots, \langle v_n, d_n\rangle \right\}$

<div style="width: 1px; height: 3rem;"></div>

$(v_n, d_n) =$ Истина, если $\langle v_n, d_n \rangle \in S$ 
$(v_n, d_n) =$ Ложь, если $\langle v_n, \neg d_n \rangle \in S$

---

### Неполные занания

Информация о $\langle v, d \rangle$ для агента $i$:

- **Полная**: $v \in \mathcal{V}_i, d \in \mathcal{D}_{v_i}$
- **Частичная**: $v \in \mathcal{V}_i, d \notin \mathcal{D}_{v_i}$, агент видит $\langle v, \bot\rangle$
- **Нет**: $v \notin \mathcal{V}_i, d \notin \mathcal{D}_{v_i}$

---

## Действия агента

Действие: $
\DeclareMathOperator{\pre}{pre}
\DeclareMathOperator{\eff}{eff}
a = \langle \pre(a), \eff(a)\rangle
$

<div style="width: 1px; height: 3rem;"></div>

$$ \pre(a) = \left\lbrace (v_i, d_i), \neg (v_j, d_j), \ldots \right\rbrace$$

$$ \eff(a) = \left\lbrace \langle v_i, \neg d_i\rangle, \langle v_j, d_j\rangle, \ldots \right\rbrace$$

---

## Задача планирования:

<div style="width: 1px; height: 3rem;"></div>

$$
\Large\mathcal{T} = \langle \mathcal{AG}, \mathcal{V}, \mathcal{A}, \mathcal{I}, \mathcal{G} \rangle
$$

---

## Описание алгоритма

1. Составить изначальный план
1. Поделиться своими знаниями с другими агентами
1. Составить распределенный план
1. Предложить уточнения к плану
1. Согласиться на финальном плане
1. Выполнить план сообща

---

## Распределенный план

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

## Уточнения к плану

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

## Угрозы плану

Пусть существует план $\prod$ где: $\langle v,d_1\rangle \in \prod$.

<div style="width: 1px; height: 3rem;"></div>

Пусть существует уточнение $\prod'$ где:
один из эффектов: $(v = d_2)$

<div style="width: 1px; height: 3rem;"></div>

$(v = d_2)$ &mdash; угроза $\prod$, так как является конфликтом

---

## Устранение угроз

В зависимости от информации о $v$:

- **Полная**: несоответствие обнаружено
- **Частичная**: агент видит $\langle v, \bot\rangle$, $\bot \neq d_1$
- **Нет**: действие не может быть выполнено

---

## Полнота алгоритма

- Мы не можем гарантировать полноту, так как количество уточнений может быть бесконечным
- Агенты используют поисковый алгоритм $A^\ast$, что приводит к достаточно хорошим уточнениям

---

## Сравнение

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg th{border-color:black;border-style:double solid;border-width:3px 1px;font-family:Noto Sans;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Noto Sans;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .hdr-big{border-color:inherit;text-align:center;vertical-align:center}
.tg .hdr-med{border-color:inherit;text-align:center;vertical-align:center;border-style:double solid solid;border-width: 3px 1px 1px}
.tg .hdr-small{border-color:inherit;text-align:center;vertical-align:center;border-style:solid solid double;border-width: 1px 1px 3px}
.tg .tg-val{border-color:inherit;text-align:right;vertical-align:center}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="hdr-big" rowspan="2">Problem</th>
    <th class="hdr-big" rowspan="2">#Agents</th>
    <th class="hdr-big" rowspan="2">%Coupling level</th>
    <th class="hdr-big" rowspan="2">#Domain actions</th>
    <th class="hdr-med" colspan="4">MAP-POP</th>
    <th class="hdr-med" colspan="4">Planning First</th>
  </tr>
  <tr>
    <th class="hdr-small">#Acts</th>
    <th class="hdr-small">#TS</th>
    <th class="hdr-small">#Partics</th>
    <th class="hdr-small">Time</th>
    <th class="hdr-small">#Acts</th>
    <th class="hdr-small">#TS</th>
    <th class="hdr-small">#Parties</th>
    <th class="hdr-small">Time</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="hdr-big">IPCSat2</td>
    <td class="hdr-big">2</td>
    <td class="hdr-big">29.3</td>
    <td class="hdr-big">2082</td>
    <td class="tg-val">21</td>
    <td class="tg-val">11</td>
    <td class="tg-val">2</td>
    <td class="tg-val">18.8</td>
    <td class="tg-val"></td>
    <td class="tg-val"></td>
    <td class="tg-val"></td>
    <td class="tg-val">&dagger;</td>
  </tr>
  <tr style="border-bottom: 3px double;">
    <td class="hdr-big">IndSat1</td>
    <td class="hdr-big">2</td>
    <td class="hdr-big">5.2</td>
    <td class="hdr-big">40</td>
    <td class="tg-val">9</td>
    <td class="tg-val">4</td>
    <td class="tg-val">2</td>
    <td class="tg-val">0.83</td>
    <td class="tg-val">9</td>
    <td class="tg-val">4</td>
    <td class="tg-val">2</td>
    <td class="tg-val">0.16</td>
  </tr>
  <tr>
    <td class="hdr-big">IPCRov2</td>
    <td class="hdr-big">1</td>
    <td class="hdr-big">2.3</td>
    <td class="hdr-big">45</td>
    <td class="tg-val">8</td>
    <td class="tg-val">4</td>
    <td class="tg-val">1</td>
    <td class="tg-val">0.39</td>
    <td class="tg-val">9</td>
    <td class="tg-val">5</td>
    <td class="tg-val">1</td>
    <td class="tg-val">0.312</td>
  </tr>
  <tr style="border-bottom: 3px double;">
    <td class="hdr-big">IndRov2</td>
    <td class="hdr-big">3</td>
    <td class="hdr-big">45.5</td>
    <td class="hdr-big">239</td>
    <td class="tg-val">36</td>
    <td class="tg-val">11</td>
    <td class="tg-val">3</td>
    <td class="tg-val">5.5</td>
    <td class="tg-val">33</td>
    <td class="tg-val">7</td>
    <td class="tg-val">3</td>
    <td class="tg-val">12.141</td>
  </tr>
  <tr>
    <td class="hdr-big">IPCLog2</td>
    <td class="hdr-big">3</td>
    <td class="hdr-big">20</td>
    <td class="hdr-big">52</td>
    <td class="tg-val">27</td>
    <td class="tg-val">9</td>
    <td class="tg-val">3</td>
    <td class="tg-val">18.187</td>
    <td class="tg-val"></td>
    <td class="tg-val"></td>
    <td class="tg-val"></td>
    <td class="tg-val">&dagger;</td>
  </tr>
  <tr>
    <td class="hdr-big">IndLog1</td>
    <td class="hdr-big">3</td>
    <td class="hdr-big">44.4</td>
    <td class="hdr-big">20</td>
    <td class="tg-val">6</td>
    <td class="tg-val">6</td>
    <td class="tg-val">2</td>
    <td class="tg-val">1.579</td>
    <td class="tg-val">9</td>
    <td class="tg-val">8</td>
    <td class="tg-val">3</td>
    <td class="tg-val">0.578</td>
  </tr>
</tbody>
</table>

---

## Вывод

Мы можем заключить, что наш алгоритм представляет собой надежную и универсальную основу для решения задач мультиагентного планирования.

---

## Спасибо за внимание
