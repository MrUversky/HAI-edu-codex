# Workshop Feedback Log

Purpose: фиксируем замечания по каркасу урока (структура, подача, этапы, файлы, формулировки).

## Entry template
- Date/time:
- Stage:
- Observation:
- Impact:
- Proposed change:
- Priority: low / medium / high
- Status: captured / shortlisted / implemented / rejected

## Implementation snapshot — 2026-04-02
- Implemented:
  - migration-first skill runtime in `.agents/skills/`
  - dispatch catalog in `workshop/dispatch-catalog.md`
  - shared case state file and `task-register` final shared-case step
  - `architecture unpacking` as a standalone lesson artifact
  - `skill-builder` guided creation runtime
  - hybrid validation skeleton with `.codex/agents/validation-orchestrator.toml` plus validation skills
  - runtime smoke-test artifact in `workshop/v1_1_runtime_smoke_test.md`
  - first concrete validation smoke-test report for `task-register`
- Partial:
  - participant-facing wording polish across all prompts and facilitator lines
  - live workshop observation of the new runtime still needs one real facilitation pass
  - tracker cleanup is in progress as the architecture continues to evolve

## Active backlog after v1.1
- participant-facing wording polish in early-stage transitions and checkpoint language
- one real facilitated pass with the new dispatch and validation runtime
- external scoring/export loop
- selective cleanup or archival of fully outdated backlog entries

### 2026-04-03 XX:XX (captured)
- Stage: shared case runtime outputs
- Observation: во время живого прогона урока shared-case skills не должны перезаписывать `shared_case/outputs/**`, потому что эта папка должна оставаться эталонной.
- Impact: если урок пишет runtime-артефакты в `shared_case/outputs/**`, эталонные примеры смешиваются со следами конкретного прогона и начинают пачкать `workbench` и потенциально `clean`.
- Proposed change: оставить `shared_case/outputs/**` как canonical examples, а runtime shared-case прогон сохранять в `shared_case/run_outputs/**`; затем обновить shared-case skills и flow-файлы на новый путь записи.
- Priority: high
- Status: implemented

### 2026-04-03 XX:XX (captured)
- Stage: shared case runtime path migration scope
- Observation: для перехода на `shared_case/run_outputs/**` уже понятен точный пакет файлов, которые нужно править; без этого решение повиснет как абстрактная идея.
- Impact: если не зафиксировать точный scope миграции, shared-case runtime продолжит писать в эталонную папку и проблема останется.
- Proposed change: при следующей итерации обновить:
  - shared-case skills:
    - `.agents/skills/shared-case-intake/SKILL.md`
    - `.agents/skills/shared-case-analysis/SKILL.md`
    - `.agents/skills/shared-case-workflow/SKILL.md`
    - `.agents/skills/shared-case-experiment/SKILL.md`
    - `.agents/skills/task-register/SKILL.md`
  - flow и orchestration docs:
    - `workshop/dispatch-catalog.md`
    - `workshop/shared-case-flow.md`
    - `workshop/start-prompt-participant.md`
    - `workshop/start-prompt-facilitator.md`
    - `workshop/demo-run-through-script.md`
    - `facilitator/facilitator-script.md`
    - `facilitator/demo-script-by-minute.md`
    - `facilitator/recovery-script.md`
  - repo artifacts:
    - добавить `shared_case/run_outputs/.gitkeep`
    - решить, нужны ли ignore-правила для runtime-файлов внутри `shared_case/run_outputs/**`
- Priority: high
- Status: implemented

### 2026-04-03 XX:XX (captured)
- Stage: repo promotion / clean vs workbench
- Observation: защита `clean`-ветки не должна опираться на `AGENTS.md`; реальный контроль нужен на уровне git-процесса и отбора изменений между `workbench` и `clean`.
- Impact: если переносить изменения слишком широко или опираться только на инструкции, в `clean` легко уедут participant-run артефакты вместо реальных улучшений урока.
- Proposed change: зафиксировать рабочий git-процесс:
  - `workbench` используется для прогонов и discovery;
  - после каждого прогона изменения делятся на `lesson improvements` и `run artifacts`;
  - в `clean` переносятся только точечные коммиты или файлы с улучшениями урока;
  - полный `merge workbench -> clean` не использовать.
- Priority: high
- Status: captured

### 2026-04-03 XX:XX (captured)
- Stage: git hygiene / local run artifacts
- Observation: в `workbench` отсутствовал `.gitignore`, поэтому participant-specific файлы и служебный мусор (`participants/<real-user>/**`, `.DS_Store`) сразу попадали в `git status`.
- Impact: повышается риск случайного коммита локальных lesson-run данных и мусора.
- Proposed change: добавить базовый repo-level `.gitignore` для:
  - `.DS_Store`
  - `participants/*` с исключениями для `participants/examples/**` и `participants/templates/**`
  - типовых skill-run артефактов вроде `raw_packet.md`, `validation_trace.md`, `validation_state.md`
  при этом не скрывать новые `SKILL.md`, чтобы потенциальные улучшения lesson runtime оставались видимыми.
- Priority: high
- Status: implemented

### 2026-04-02 15:XX (captured)
- Stage: lesson entrypoint UX
- Observation: для живого запуска урока нужны ещё более короткие participant-facing входные команды уровня `запусти урок в participant mode` / `запусти урок в facilitator mode`, а не только длинные стартовые prompts.
- Impact: без короткого входа старт урока остаётся слишком техническим и тяжёлым для реального запуска.
- Proposed change: добавить в dispatch layer два канонических верхнеуровневых entrypoint-action:
  - короткий запуск урока для участника
  - короткий запуск урока для ведущего
  при этом полная логика режима остаётся в `start-prompt-participant.md` и `start-prompt-facilitator.md`.
- Priority: high
- Status: implemented

### 2026-04-02 15:XX (captured)
- Stage: language policy / participant-facing copy
- Observation: в participant-facing и facilitator-facing слое осталось слишком много англицизмов (`entrypoint`, `dispatch`, `mode`, `skill`, `runtime` и т.д.), хотя урок ведётся на русском и должен звучать естественно.
- Impact: англицизмы повышают когнитивную нагрузку, делают объяснение менее естественным и ухудшают восприятие урока русскоязычной аудиторией.
- Proposed change: зафиксировать явное языковое правило:
  - participant-facing и facilitator-facing коммуникация по умолчанию на русском
  - англицизмы заменяются русскими эквивалентами везде, где это не ломает техническую точность
  - технические англоязычные термины допускаются только как названия файлов, системных сущностей или неизбежных терминов Codex
  - отдельно проверить `AGENTS.md`, `workshop/dispatch-catalog.md`, стартовые prompts и flow-файлы на избыточные англицизмы
- Priority: high
- Status: partial

### 2026-04-02 15:XX (captured)
- Stage: setup personalization continuity
- Observation: после того как имя участника собрано на этапе setup, помощник дальше не использует его в обращении, из-за чего вопрос про имя выглядит формальным и неработающим.
- Impact: персонализация урока ощущается непоследовательной, а собранный контекст не используется в коммуникации.
- Proposed change: добавить в participant-facing инструкции правило:
  - после сохранения `participant_setup.md` помощник использует имя участника дальше по уроку там, где это уместно;
  - обращение должно быть естественным и умеренным, без повторения имени в каждом сообщении.
- Priority: medium
- Status: implemented

### 2026-04-02 15:XX (captured)
- Stage: setup explanation-style question
- Observation: вопрос про предпочтительный формат объяснений не должен быть открытым; лучше предложить 3 понятных варианта и потом реально следовать выбранному стилю в ходе урока.
- Impact: открытый вопрос создаёт лишнее трение, а без явной привязки к дальнейшему поведению выбор стиля выглядит декоративным.
- Proposed change: заменить свободный вопрос на выбор из 3 фиксированных стилей объяснения и добавить в инструкции правило, что помощник обязан подстраивать подачу под выбранный стиль.
- Priority: high
- Status: implemented

### 2026-04-02 15:XX (captured)
- Stage: shared case transition phrasing
- Observation: фраза вроде `Сохрани и покажи следующий шаг` описана некорректно: она скрывает, что помощник фактически уже выполняет следующий шаг, и не объясняет, что именно произойдёт дальше.
- Impact: переходы между шагами цепочки выглядят размыто; участник не понимает, где заканчивается сохранение артефакта и где начинается следующий этап.
- Proposed change: для всей shared-case цепочки заменить такие переходы на более точные формулировки:
  - отдельно подтвердить сохранение текущего артефакта
  - отдельно назвать следующий этап
  - отдельно сказать, какой именно артефакт появится на следующем шаге
  - не маскировать запуск следующего шага под нейтральную фразу `покажи следующий шаг`
- Priority: high
- Status: partial

### 2026-04-02 15:XX (captured)
- Stage: upstream skill architecture
- Observation: `telegram-digest` и `review-monitor` не должны производить финальные полезные выводы; по целевой архитектуре они должны собирать и нормализовать сырой пакет данных, который потом обрабатывает основная цепочка skills.
- Impact: если эти skills вести как самостоятельные "финальные" преобразователи, ломается общая логика пайплайна и дублируется работа `shared-case-intake` и следующих шагов.
- Proposed change: зафиксировать архитектурное правило:
  - `telegram-digest` и `review-monitor` — это входные skills сбора сырья;
  - их output contract = `сырой пакет данных для дальнейшей обработки`;
  - `shared-case-intake` и общий downstream pipeline должны уметь работать не только со стандартными `shared_case/inputs/*`, но и с таким подготовленным сырьевым пакетом.
- Priority: high
- Status: implemented

### 2026-04-02 15:XX (captured)
- Stage: upstream skill questioning
- Observation: для `telegram-digest` и `review-monitor` список вопросов не должен быть длинным и "продуктовым", потому что на этом этапе мы собираем только сырой пакет данных.
- Impact: длинный список вопросов создаёт лишнюю тяжесть и уводит участника в преждевременное проектирование конечного результата.
- Proposed change: сократить participant-facing вопросы для upstream skills до минимального набора:
  - источник данных;
  - период или объём выборки, если это важно;
  - что сохранить в сырой пакет;
  - что человек должен быстро проверить перед передачей дальше.
- Priority: high
- Status: implemented

### 2026-04-02 15:XX (captured)
- Stage: upstream skill run timing
- Observation: на этапе выбора и проектирования upstream skill не нужно спрашивать про конкретный чат, конкретный экспорт или конкретный файл выгрузки, если сами данные будут переданы только в момент реального запуска skill.
- Impact: участнику задаются лишние операционные вопросы слишком рано, и create/adapt stage смешивается с runtime шагом.
- Proposed change: для простых upstream skills разделить:
  - на этапе проектирования фиксируется только роль skill и общий contract входа;
  - конкретный экспорт, чат или файл указывается уже в момент реального запуска skill.
- Priority: high
- Status: implemented

### 2026-04-02 15:XX (captured)
- Stage: post-validation practice check
- Observation: после того как skill создан и провалидирован, участнику полезно по возможности проверить его на практике, а не останавливаться на spec и validation report.
- Impact: без практического прогона этап create/adapt может ощущаться слишком теоретическим, а участник не видит, работает ли skill на реальном входе.
- Proposed change: добавить после validation дополнительный шаг или явную опцию:
  - `проверь skill на практике`
  - прогнать skill на одном реальном или тестовом входе
  - коротко зафиксировать, что сработало, что не сработало и что нужно поправить
- Priority: high
- Status: implemented

### 2026-04-03 00:XX (captured)
- Stage: external intake strictness
- Observation: при прогоне внешнего сырого пакета через intake помощник слишком легко подтягивает накопленный контекст репозитория и предыдущего разговора, из-за чего `intake` соскальзывает в ранний `analysis` и начинает "достраивать" картину вместо простой структуризации текущего входа.
- Impact: шаг `intake` теряет чистоту, появляются домыслы и хардкод из прошлого контекста, а downstream-цепочка получает уже частично интерпретированный материал.
- Proposed change: для внешних сырьевых пакетов добавить более жёсткий режим или отдельный intake-skill с правилами:
  - использовать только текущий `raw_packet`
  - не опираться на предыдущие shared-case outputs и прошлый conversational context
  - не переходить к причинам, выводам и красивой педагогической сборке
  - по возможности сохранять traceability между блоками результата и наблюдаемыми фрагментами входа
- Priority: high
- Status: partial

### 2026-04-03 00:XX (captured)
- Stage: validation agent demonstration gap
- Observation: `validation-orchestrator` уже описан как кастомный агент и связан с несколькими validation skills, но в уроке это пока не показывается участнику как реальный агентный запуск; со стороны UX validation всё ещё выглядит просто как “ещё одна проверка”.
- Impact: участник не видит разницу между skill и агентом-координатором, а одна из важных идей hybrid-архитектуры остаётся скрытой.
- Proposed change: добавить в lesson flow и participant/facilitator guidance явную демонстрацию:
  - что на этапе validation запускается именно `validation-orchestrator`;
  - что он последовательно вызывает несколько validation skills;
  - что итог собирается в единый `validation_report`;
  - по возможности сохранить trace-артефакт вроде `validation_trace.md` или `validation_state.md`, чтобы handoff внутри validation был видимым.
- Priority: high
- Status: implemented

## Entries

### 2026-04-02 14:XX (captured)
- Stage: shared case walkthrough
- Observation: контрольный вопрос на понимание прозвучал не к месту в текущем темпе.
- Impact: сбивает поток и ощущение «идём по сценарию».
- Proposed change: в participant mode не вставлять спонтанные check-вопросы без явного запроса; держать объяснение линейным.
- Priority: high
- Status: captured

### 2026-04-02 14:31 (captured)
- Stage: setup
- Observation: формулировка вопроса про уровень AI с «+ 1 фраза» лишняя и неестественная; нужен простой выбор уровня.
- Impact: участнику непонятен формат ответа, создается лишняя когнитивная нагрузка.
- Proposed change: оставить только перечисление уровней (`начинающий / средний / продвинутый`) без дополнительного требования.
- Priority: high
- Status: captured

### 2026-04-02 14:31 (captured)
- Stage: shared case intro
- Observation: пример «было/стало» слишком привязан к конкретному кейсу урока и не объясняет, что значит «после цепочки».
- Impact: участникам без контекста непонятно, где именно происходит преобразование и что является результатом.
- Proposed change: стандартизировать формулировку примеров как `сырой вход -> обработка агентами -> выходной артефакт` и давать 1 общий (универсальный) пример + 1 кейсовый.
- Priority: high
- Status: captured

### 2026-04-02 14:31 (captured)
- Stage: переход setup -> shared case
- Observation: переход «следующий этап по сценарию shared-case-flow» звучит внутренне и не объясняет участнику, что сейчас будет происходить в формате ведущий/участник.
- Impact: участник теряет контекст роли и ожидаемых действий на своем локальном репо.
- Proposed change: добавить participant-facing переходный блок: что показывает ведущий, что делает участник локально, где можно открыть подробности, какой ожидаемый результат этапа.
- Priority: high
- Status: captured

### 2026-04-02 14:31 (captured)
- Stage: live facilitation sync
- Observation: нужно лучше синхронизировать действия ведущего и участников (кто что делает одновременно).
- Impact: риск рассинхрона, разные участники оказываются на разных шагах.
- Proposed change: добавить в flow-файлы явные sync-подсказки: `Ведущий делает`, `Участник делает`, `Сигнал перехода к следующему шагу`.
- Priority: high
- Status: captured

### 2026-04-02 14:31 (captured)
- Stage: checkpoints / questions
- Observation: вопросы после этапа должны быть заранее определены по типу и месту, а не случайные.
- Impact: случайные вопросы могут ломать темп и восприниматься «не в тему».
- Proposed change: ввести stage-based наборы допустимых checkpoint-вопросов и лог их ответов в отдельный файл.
- Priority: medium
- Status: captured

### 2026-04-02 14:31 (captured)
- Stage: assessment architecture
- Observation: нужна идея внешней оценки результатов (отправка артефактов во внешний сервис и возврат оценки с сохранением локально).
- Impact: сейчас нет замкнутого контура сбора результатов и централизованного scoring.
- Proposed change: добавить discovery-задачу: определить контракт экспорта артефактов, способ отправки, формат ответа со score, и локальное сохранение результата.
- Priority: medium
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: shared case core logic
- Observation: в текущем объяснении и flow возникает логический разрыв: shared case выглядит как ручной разбор файлов, хотя по замыслу входные материалы должны обрабатываться агентами.
- Impact: участник не понимает, что именно он должен делать в системе; теряется сама идея agent workflow, а упражнение деградирует в чтение готовых markdown-файлов.
- Proposed change: явно зафиксировать в flow, что `shared_case/inputs/*` — это входы для запуска цепочки агентов, `shared_case/outputs/*` — ожидаемые результаты обработки, а действие участника/ведущего на этапе должно быть сформулировано как `запусти/прогони агент(ов)`, а не `прочитай и выпиши`.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: shared case execution model
- Observation: не описано, каким именно способом участник должен "запустить агентов" в своей локальной копии и как это синхронизируется с тем, что показывает ведущий.
- Impact: даже если идея multi-agent flow понятна концептуально, участник не получает операционной инструкции и не может воспроизвести шаг у себя.
- Proposed change: добавить в shared-case этап явную модель исполнения с тремя блоками: `что запускает ведущий`, `что запускает участник локально`, `какой артефакт должен появиться после запуска`.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: lesson operating model
- Observation: в каркасе недостаточно явно описаны три стороны урока: ведущий онлайн, участник в локальной копии репозитория и помощник Codex внутри локального окружения участника.
- Impact: непонятно, кто именно инициирует шаг, кто показывает материал, кто выполняет локальное действие и кто поддерживает участника по ходу урока.
- Proposed change: для каждого этапа добавить операционный шаблон `Ведущий`, `Участник`, `Codex-помощник` с четким распределением ролей.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: stage tracking
- Observation: помощник не фиксирует явно текущий этап урока, статус прохождения и следующий шаг участника.
- Impact: участник теряет ощущение прогресса и не понимает, что уже завершено и что делать дальше.
- Proposed change: на каждом переходе объявлять `Текущий этап`, `Что уже сделано`, `Что сейчас делаем`, `Что будет результатом шага`.
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: participant prompt design
- Observation: participant-facing инструкция для запуска Intake Agent пока слишком длинная и техническая; участнику нужен короткий, естественный вызов вроде `запусти intake агента и покажи результат`.
- Impact: длинный prompt отвлекает от ощущения "магии" и от самой механики агентной обработки.
- Proposed change: сделать двухслойную модель вызова: короткая команда для участника и скрытая/встроенная инструкция для помощника, где уже описано, какие файлы читать и какой output produce.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: agent invocation UX
- Observation: в текущем репо нет явного, простого механизма вызова markdown-агентов по коротким командам или ключевым словам.
- Impact: участник не понимает, как именно "запустить агента"; приходится вручную перечислять файлы и роль в prompt.
- Proposed change: определить repo-level convention для вызова агентов (например, через AGENTS.md/start prompt/dispatch rules), чтобы короткие команды маппились на конкретные agent spec files и input/output paths.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: output routing
- Observation: участнику не объясняется, куда должен пойти результат работы агента: просто показать в чате, сохранить в файл, сравнить с эталоном, или передать следующему агенту.
- Impact: шаг выглядит незавершенным, а chain-of-agents не ощущается как настоящая цепочка обработки.
- Proposed change: для каждого запуска агента явно указывать `что показать`, `что сохранить`, `что идет на следующий шаг`.
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: rule system / agent dispatch
- Observation: текущая идея `repo-level rules` слишком расплывчата; пользователю нужен внятный аналог Cursor Rules / CodeMD с жестким и предсказуемым поведением, а не просто набор markdown-заметок.
- Impact: без явного механизма диспетчеризации Codex выглядит как менее полный инструмент для agentic workflow внутри репозитория.
- Proposed change: спроектировать явный слой dispatch-правил для workshop-репозитория: короткая пользовательская команда -> конкретный agent spec -> конкретные input paths -> конкретный output path -> следующий шаг цепочки.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: codex capabilities explanation
- Observation: пользователю нужно четко объяснить, какие типы инструкций в Codex реально исполняются автоматически, а какие являются только текстовыми указаниями для модели.
- Impact: без этого трудно проектировать надежный UX и ожидания от инструмента.
- Proposed change: в документации воркшопа добавить отдельный блок `Что в Codex является правилами, что является конвенцией, что является автоматизацией`.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: rules architecture decision
- Observation: для воркшопа приоритетом является portability между средами (`Codex`, `Cursor`, `Claude` и т.д.), поэтому решение должно по возможности оставаться `MD-only`, без обязательных локальных скриптов и host-specific automation.
- Impact: script-based execution layer может дать больше жесткости, но ухудшит переносимость и усложнит учебный каркас.
- Proposed change: сначала спроектировать максимально строгую и переносимую архитектуру на основе `AGENTS.md` + markdown-конвенций вызова агентов; скрипты рассматривать только как опциональный локальный enhancement, а не как основу решения.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: AGENTS.md improvement scope
- Observation: текущий `AGENTS.md` задает общие правила работы, но не выступает полноценным dispatch layer для коротких пользовательских команд и маршрутизации agent workflow.
- Impact: короткие participant-facing команды не получают достаточно жесткой, предсказуемой интерпретации.
- Proposed change: расширить `AGENTS.md` или связанный markdown-слой так, чтобы в нем были явно описаны: shorthand-команды, mapping на agent files, входы/выходы, порядок цепочки и ожидаемое поведение помощника.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: MD dispatch layer design
- Observation: dispatch layer должен интерпретировать не только точные команды, но и естественные participant-facing формулировки с близким намерением (`обработай сырые данные`, `запусти intake`, `покажи первый результат`) без расползания в произвольную трактовку.
- Impact: если слой понимает только жесткие фразы, UX будет хрупким; если трактует слишком свободно, поведение станет непредсказуемым.
- Proposed change: задать для каждого агента `intent patterns`, допустимые синонимы и границы интерпретации, а также правило fallback: при неоднозначности помощник обязан уточнить или предложить список доступных agent actions.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: maintainability of dispatch layer
- Observation: при добавлении нового агента в репозиторий должна обновляться и dispatch-конфигурация; иначе agent catalog и participant commands расходятся.
- Impact: система быстро потеряет консистентность и расширяемость.
- Proposed change: ввести repo convention: новый агент считается неполным, пока для него не добавлены dispatch-entry, input/output contract и participant-facing command examples.
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: shared case magic / operational output
- Observation: текущая цепочка `Intake -> Analysis -> Workflow -> Experiment` логична, но воспринимается скорее как последовательность prompt-based преобразований текста, а не как переход к реальному рабочему процессу.
- Impact: участнику не хватает ощущения "магии" и ощутимого операционного результата; shared case заканчивается на уровне осмысления, а не на уровне рабочего артефакта.
- Proposed change: добавить после `Experiment Agent` новый обязательный агент рабочего выхода, предварительное название: `Task Register Agent` или `Sprint Planning Agent`.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: new agent proposal / Task Register Agent
- Observation: после выбора первого пилота нужен дополнительный шаг, который превращает pilot card в конкретный план действий, ближе к реальному рабочему процессу.
- Impact: без этого финал shared case остаётся слишком концептуальным и не демонстрирует переход от анализа к исполнению.
- Proposed change: спроектировать нового агента со следующей ролью:
  - берет `pilot card` и связанные outputs предыдущих шагов
  - формирует `goal for first sprint`
  - формирует `task register / action list`
  - добавляет `owner placeholders`
  - отмечает `dependencies / blockers`
  - добавляет `success checks`
  - сохраняет результат в отдельный явный артефакт, например `shared_case/outputs/task_register.md`
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: lesson flow expansion
- Observation: если добавляется агент рабочего выхода, нужно обновить весь lesson flow от начала до конца, чтобы было ясно, что shared case завершается не на pilot card, а на operational artifact.
- Impact: без обновления общего flow новый агент будет выглядеть как случайная надстройка, а не как органичная часть lesson architecture.
- Proposed change: пересобрать целевой flow воркшопа в таком виде:
  - Intake
  - Analysis
  - Workflow
  - Experiment
  - Task Register / Sprint Planning
  - затем architecture unpacking / mini-practice / create-adapt / validation / personal next step
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: task register artifact design
- Observation: новый финальный артефакт shared case должен быть не абстрактным summary, а чем-то, что выглядит как реальный рабочий документ.
- Impact: именно этот артефакт может создать ощущение "из хаоса пришли к рабочему плану", которого сейчас не хватает.
- Proposed change: для `task_register.md` предусмотреть такие секции:
  - first sprint goal
  - in-scope tasks
  - out-of-scope tasks
  - owner placeholders
  - dependencies / blockers
  - first review checkpoint
  - success criteria for sprint
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: target agent spec / Task Register Agent
- Observation: нужен явный target-spec нового агента, чтобы было понятно, какой именно operational step мы хотим добавить в shared case.
- Impact: без agent spec идея остаётся на уровне пожелания и её трудно встроить в lesson architecture, templates и dispatch layer.
- Proposed change: целевая спецификация нового агента:

  `# Task Register Agent`

  `## Role`
  `You are the Task Register Agent. Your role is to convert a selected first pilot into a concrete, bounded first-sprint task register that a human team could realistically review and act on.`

  `## Job to be done`
  `Help the team move from a pilot concept to an operational starting plan with explicit tasks, boundaries, placeholders for ownership, dependencies, and a first review checkpoint.`

  `## Inputs`
  `You receive:`
  `- pilot use case`
  `- scope boundaries`
  `- what is needed to start`
  `- success criteria`
  `- key constraints if relevant`

  `## Process`
  `1. Restate the first sprint goal in one sentence.`
  `2. Break the pilot into a small set of concrete first-sprint tasks.`
  `3. Separate in-scope tasks from out-of-scope tasks.`
  `4. Add owner placeholders where ownership is required.`
  `5. Mark dependencies, blockers, or unknowns.`
  `6. Define the first review checkpoint.`
  `7. Restate success criteria for the sprint in observable terms.`

  `## Output format`
  `Return these sections:`
  `1. First sprint goal`
  `2. In-scope tasks`
  `3. Out-of-scope tasks`
  `4. Owner placeholders`
  `5. Dependencies and blockers`
  `6. First review checkpoint`
  `7. Sprint success criteria`

  `## Guardrails`
  `- Do not invent confirmed owners when ownership is unknown.`
  `- Do not hide blockers or external dependencies.`
  `- Do not expand the sprint beyond a realistic first slice.`
  `- Do not turn a pilot into a broad transformation roadmap.`
  `- Do not assume live integrations unless they are explicitly available.`

  `## Escalation to human`
  `Escalate when:`
  `- ownership is politically sensitive or unknown,`
  `- dependencies span multiple teams or systems,`
  `- the sprint cannot be bounded cleanly,`
  `- or success criteria are not realistically observable.`

- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: architecture unpacking flow
- Observation: этап `architecture unpacking` в текущем репо существует только как часть скриптов и prompt-файлов и не оформлен как отдельный, явный teaching artifact.
- Impact: после shared case непонятно, что именно должен объяснить помощник или ведущий, и какие тезисы участник должен унести как ментальную модель.
- Proposed change: добавить отдельный явный блок `architecture unpacking` для цепочки уже из пяти агентов (`Intake -> Analysis -> Workflow -> Experiment -> Task Register`) и зафиксировать в нём, что именно объясняется после shared case.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: architecture unpacking content
- Observation: после добавления пятого агента нужно обновить объяснение "почему не один агент", иначе lesson explanation останется устаревшим и будет расходиться с фактическим flow.
- Impact: участники увидят одну цепочку, а услышат объяснение, рассчитанное на другую архитектуру.
- Proposed change: в teaching content для этого этапа зафиксировать такие тезисы:
  - `Intake` нужен, чтобы превратить хаос в структуру без преждевременных выводов
  - `Analysis` нужен, чтобы отделить сигналы и tensions от просто списка фактов
  - `Workflow` нужен, чтобы превратить понимание проблемы в повторяемый процесс
  - `Experiment` нужен, чтобы сузить процесс до первого реалистичного пилота
  - `Task Register` нужен, чтобы перевести пилот в конкретный рабочий план и задачи
  - разделение на агентов сохраняет качество handoff и не даёт одному prompt делать всё сразу
  - человек остаётся нужен на этапах интерпретации, выбора scope, ownership и финального решения
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: lesson flow update after 5th agent
- Observation: после расширения shared case до пяти агентов нужно явно обновить lesson flow и participant guidance, чтобы этот новый конец shared case не потерялся.
- Impact: без этого участники и ведущий будут считать, что shared case заканчивается на `Experiment`, хотя новый целевой конец — это `Task Register`.
- Proposed change: обновить целевой порядок shared case в lesson materials:
  - Intake
  - Analysis
  - Workflow
  - Experiment
  - Task Register
  - затем Architecture unpacking
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: agent handoff model
- Observation: сейчас chain-of-agents фактически держится на контексте чата и устном подтверждении, а не на явных handoff artifacts между агентами.
- Impact: цепочка выглядит менее полноценной, результаты трудно корректировать и подтверждать, а следующий агент опирается не на зафиксированный approved output, а на текущий conversational context.
- Proposed change: ввести для каждого агентного шага единый handoff pattern:
  - агент сначала показывает `draft` результата
  - человек при необходимости вносит правки или даёт approve
  - после approve результат сохраняется как официальный step artifact
  - следующий агент работает только с этим сохранённым artifact, а не с чатом
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: approval and persistence
- Observation: в текущем lesson flow не описан момент подтверждения результата агентного шага и записи его в устойчивое хранилище репозитория.
- Impact: участник не видит жизненный цикл результата: proposal -> review -> approved artifact -> downstream use.
- Proposed change: для каждого шага shared case добавить явную фазу:
  - `Draft shown`
  - `Human review`
  - `Approved and saved`
  - `Passed to next agent`
  а также определить path для каждого approved artifact.
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: memory and state strategy
- Observation: нужно решить, где хранить долговременное состояние цепочки: только в step files, или дополнительно в одном summary/memory artifact.
- Impact: без этого непонятно, как агентам быстро ориентироваться в уже утверждённых результатах и как восстанавливать run после паузы или сбоя.
- Proposed change: начать с простой модели без лишней сложности:
  - каждый шаг сохраняет approved output в отдельный файл
  - опционально добавляется один lightweight `run memory` или `shared_case_state.md`, который перечисляет последние утверждённые артефакты и текущий этап
  - не вводить сложную memory-system до тех пор, пока step-artifacts не описаны чётко
- Priority: medium
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: standard handoff pattern
- Observation: нужен единый, повторяемый стандарт агентного шага, который одинаково работает для всех агентов в lesson flow и меняется только по конкретным input/output paths и структуре артефакта.
- Impact: без общего стандарта каждый шаг будет оформлен по-разному, а participant experience и handoff quality будут плавать от этапа к этапу.
- Proposed change: принять единый step pattern для всех агентов:

  `1. Input source`
  `- какой approved artifact или raw input читает агент`

  `2. Agent run`
  `- агент выполняет только свою узкую роль`

  `3. Draft output`
  `- агент показывает черновик результата в чате`
  `- человек может внести правку или попросить переработку`

  `4. Human review`
  `- человек либо approve, либо возвращает на revision`

  `5. Approved artifact`
  `- после approve результат сохраняется в официальный step file`

  `6. Handoff`
  `- следующий агент читает только approved artifact, а не conversational context`

  `7. Step state`
  `- при необходимости обновляется lightweight state summary с текущим этапом и списком approved artifacts`

  `Стандартные поля для описания каждого шага:`
  `- Step name`
  `- Agent spec file`
  `- Reads from`
  `- Draft shown as`
  `- Approved file path`
  `- Next agent`
  `- Human review question`

- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: architecture unpacking teaching point
- Observation: в `architecture unpacking` нужно явно объяснять не только разделение ролей между агентами, но и хороший operational pattern `draft -> human review -> approve -> save -> handoff`.
- Impact: без этого участник не увидит, чем agent system отличается от обычного чата с длинным контекстом и почему сохранённые артефакты повышают качество и устойчивость процесса.
- Proposed change: добавить в teaching content этого этапа явное объяснение:
  - хороший агентный workflow не держится только на контексте чата
  - результат шага сначала показывается как draft
  - человек утверждает или корректирует его
  - approved result сохраняется как step artifact
  - следующий агент работает уже с этим artifact
  - именно это делает систему более надёжной, проверяемой и восстанавливаемой, чем простой chat flow
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: mini-practice necessity
- Observation: если участник проходит `shared case` руками у себя локально вместе с ведущим, `mini-practice` в текущем виде начинает дублировать уже полученный hands-on опыт.
- Impact: урок растягивается без добавления новой учебной ценности, а этап выглядит искусственно вставленным.
- Proposed change: для текущей версии урока считать `mini-practice` необязательным или убрать его как отдельный шаг; альтернативно вернуть его только если появится отдельный, существенно другой mini-case.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: create/adapt agent transition
- Observation: при входе в этап `create or adapt agent` помощник должен явно распознавать смену стадии урока и переключаться в режим выбора/проектирования собственного агента участника.
- Impact: без явного перехода участнику неочевидно, что теперь мы уже не разбираем общий кейс, а начинаем собирать его собственного агента.
- Proposed change: на старте этого этапа помощник должен:
  - объявить текущий этап
  - кратко объяснить цель этапа
  - предложить выбор: адаптировать существующего elective-agent или создать похожего с нуля
  - показать доступные заготовки / шаблоны
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: create/adapt agent UX
- Observation: участнику нужно сразу предложить понятные варианты выбора, а не ждать, что он сам пойдёт читать весь каталог агентов и шаблонов.
- Impact: иначе растёт трение в начале самого важного практического этапа.
- Proposed change: participant-facing вход в этап должен включать:
  - список доступных elective agents с 1-строчным объяснением
  - опцию `создать похожего агента под свой сценарий`
  - опцию `адаптировать существующего`
  - опору на `agent_spec_template.md`
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: create/adapt agent process design
- Observation: для участника пока не описан чёткий процесс выбора и сборки собственного агента после перехода на этот этап.
- Impact: даже если каталог агентов есть, участник не понимает, что делать после фразы `хочу такого-то агента`.
- Proposed change: описать единый participant flow:
  - выбрать место агента в цепочке: `upstream collector` / `processor` / `downstream sync`
  - выбрать ближайший starter-agent или вариант `create similar`
  - определить `input`, `output`, `human checkpoint`
  - собрать draft agent spec по `agent_spec_template.md`
  - при необходимости добавить integration stub
  - сохранить в canonical participant path
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: skill-creator vs workshop agents
- Observation: встроенный `skill-creator` не является хорошим каноническим entrypoint для этого этапа, потому что он ориентирован на создание Codex skills, а не workshop-agent specs внутри репозитория.
- Impact: если использовать его как основной путь, участники смешают понятия `skill`, `agent`, `integration stub` и уйдут в техническую сторону вместо bounded agent design.
- Proposed change: для воркшопа считать каноническим путь через repo templates (`agent_spec_template.md`, `integration_stub_template.md`), а `skill-creator` использовать только как внутренний advanced tool для будущих авторов репозитория, но не как participant-facing workflow.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: canonical storage for participant agents
- Observation: не задано единое место хранения созданных или адаптированных агентных артефактов участника.
- Impact: валидация, дальнейшая навигация и сбор submission package становятся разнородными и хрупкими.
- Proposed change: ввести canonical path convention, например:
  - `participants/<name>/agents/<agent_slug>/created_or_adapted_agent.md`
  - `participants/<name>/agents/<agent_slug>/integration_stub.md` (optional)
  - `participants/<name>/agents/<agent_slug>/validation_report.md`
  и использовать эти пути как стандарт для validation и submission.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: elective agent catalog redesign
- Observation: текущий каталог elective agents полезен, но ещё не объясняет участнику, как каждый агент встраивается в общую workflow architecture.
- Impact: агенты воспринимаются как отдельные идеи, а не как модули, которые можно встроить в начало, середину или конец цепочки.
- Proposed change: переупаковать elective agents по роли в потоке:
  - `upstream collectors`: агенты, которые собирают raw inputs из источников или экспортов
  - `processors / analyzers`: агенты, которые структурируют, анализируют или выделяют сигналы
  - `downstream sync / action agents`: агенты, которые раскладывают результат по задачам, системам или digest outputs
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: notion agent positioning
- Observation: `Notion Sync Agent` логичнее показывать не как абстрактный агент "про Notion", а как downstream-agent, который принимает уже подготовленный результат цепочки и раскладывает его в structured Notion-ready representation.
- Impact: так участнику проще понять, зачем этот агент нужен и где он встраивается в workflow.
- Proposed change: в participant guidance позиционировать `Notion Sync Agent` как агент финального раскладывания результатов, задач, follow-ups и owner placeholders после анализа/планирования, а не как первый шаг цепочки.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: telegram agent positioning
- Observation: `Telegram Digest Agent` логичнее показывать как upstream collector / noise-reduction agent, который превращает поток сообщений или экспорт чата в usable raw input bundle для дальнейшей обработки.
- Impact: это делает его место в системе очевидным и уменьшает страх перед "интеграцией с Telegram" как чем-то слишком большим.
- Proposed change: participant guidance должна показывать `Telegram Digest Agent` как early-stage agent, который может собирать или нормализовать message exports в initial digest / grouped input, желательно в stub or export-based mode.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: analytics agent fit
- Observation: `Analytics Insight Agent` сейчас выглядит слабее в воркшопе, потому что требует либо готовых экспортов, либо доступа к данным, которого у многих участников нет под рукой.
- Impact: агент кажется менее доступным и больше напоминает обычную работу с ChatGPT над таблицей, если не задать чёткий source model.
- Proposed change: ограничить participant-facing версию так:
  - default input — CSV/Google Sheets export/manual metric snapshot
  - без обещаний live data access
  - с очень чётким contract: anomalies, likely drivers, caveats, next checks
  либо понизить приоритет этого агента в базовом каталоге.
- Priority: medium
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: new elective option / resume analysis
- Observation: для HR-контекста не хватает более очевидного и instantly relatable elective agent, чем текущий набор.
- Impact: участникам из HR или recruiting сложнее быстро увидеть “своего” агента в каталоге.
- Proposed change: добавить новый elective candidate, например `Resume Analysis Agent`, с явным contract:
  - inputs: CV/resume text, vacancy criteria, optional interviewer notes
  - outputs: normalized candidate summary, fit signals, open questions, risk flags, next review recommendation
  - guardrails: no hiring decision automation, no hidden scoring claims, human review required
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: integration guidance clarity
- Observation: агенты с внешними системами или источниками могут пугать участников, если не показать безопасный путь `stub / export / prepared input` вместо live integration.
- Impact: участники могут отказаться от хорошего сценария просто потому, что он выглядит как слишком технический.
- Proposed change: для каждого elective agent в participant guidance явно указывать один из режимов:
  - `text-only`
  - `export-based`
  - `stub integration`
  - `live integration (advanced)`
  и по умолчанию вести участников через первые три, а не через live mode.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: storage model correction
- Observation: хранение созданных агентных артефактов в `participants/...` не подходит как каноническая модель; участник работает в своей локальной копии репозитория, и агент должен выглядеть как часть агентного каталога, а не как персональная папка.
- Impact: модель хранения через `participants/...` делает агент визуально второстепенным и усложняет объяснение структуры репозитория.
- Proposed change: для created/adapted agent использовать canonical repo-level storage внутри агентного слоя, например `agents/custom/` или `agents/adapted/`, а participant outputs оставлять в `participants/` только для финальных личных артефактов урока.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: terminology simplification
- Observation: participant-facing объяснения этапа create/adapt agent не должны использовать англоязычные технические категории вроде `upstream`, `processor`, `downstream`, `text-only`, `export-based` без явной русской интерпретации.
- Impact: такие термины создают лишнее трение и делают процесс менее понятным для русскоязычного воркшопа.
- Proposed change: использовать русские категории:
  - `агент, который собирает входящие данные`
  - `агент, который разбирает и структурирует`
  - `агент, который раскладывает результат в задачи или систему`
  а технические режимы объяснять простыми словами, если они вообще нужны.
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: skill-creator clarification
- Observation: участнику и фасилитатору нужно прямо объяснить, зачем нужен `skill-creator` и почему он не является основным путём создания workshop-agent в этом уроке.
- Impact: иначе возникает ложное ожидание, что встроенный инструмент Codex должен быть обязательной частью participant flow.
- Proposed change: зафиксировать, что:
  - `skill-creator` нужен для создания Codex skills
  - workshop agent в рамках урока — это прежде всего markdown-spec агента
  - участник по умолчанию не использует `skill-creator`
  - `skill-creator` остаётся опциональным advanced tool для авторов репозитория, а не для базового сценария урока
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: create/adapt agent simplification
- Observation: этап нужно упростить до нескольких понятных вопросов, чтобы участник не разбирался в `MCP`, коде и типах интеграций до того, как появится базовый агентный контракт.
- Impact: без этого этап выглядит технически тяжёлым и распадается на слишком много абстракций.
- Proposed change: сделать базовый participant flow через 4 вопроса:
  - какая повторяющаяся ситуация у тебя есть
  - что приходит на вход
  - что должно получаться на выходе
  - где человек должен проверить или подтвердить результат
  после ответов помощник:
  - предлагает ближайшего готового агента или вариант `создать похожего`
  - собирает markdown-spec агента
  - если есть внешняя система, помечает её как предположение или заглушку, а не как обязательную реализацию
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: agent vs implementation boundary
- Observation: в уроке нужно чётко развести понятия `агент как спецификация` и `агент как реально реализованная интеграция с кодом/MCP`.
- Impact: без этой границы участник не понимает, должен ли он на этом этапе писать код, подключать API или достаточно описать поведение агента.
- Proposed change: явно объяснить:
  - в базовом сценарии воркшопа агент = markdown-описание роли, входов, выходов, guardrails и human checkpoints
  - код, MCP и live integrations не обязательны
  - если интеграция не доступна, она описывается как заглушка или предположение
  - реализация кода — это отдельный, более продвинутый слой, не обязательный для прохождения урока
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: agent builder concept
- Observation: для этапа `create/adapt agent` нужен не generic `skill creator`, а специальный агент-конструктор воркшопа, который помогает собрать агента ближе к реальности и по единым правилам репозитория.
- Impact: без такого конструктора участник либо остаётся на уровне абстрактного markdown-описания, либо уходит в слишком свободное и неструктурированное проектирование.
- Proposed change: спроектировать отдельного `Agent Builder` (или `Agent Creator`) со следующей ролью:
  - распознаёт, что участник находится на этапе создания агента
  - предлагает выбор из 4 фокусных сценариев:
    - Telegram Digest
    - Review Monitor
    - Notion Sync
    - Resume Analysis
  - ведёт участника по общим универсальным правилам создания агента
  - создаёт agent spec
  - при необходимости подсказывает структуру файлов, scripts и integration guide
  - подготавливает артефакт к следующему шагу validation
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: agent builder universal rules
- Observation: если создавать агентов "ближе к реальности", нужен единый набор правил, где что лежит, как называется и как устроена минимальная файловая структура.
- Impact: без этого у каждого агента получится своя структура, и урок не будет выглядеть как единая инженерная практика.
- Proposed change: в спецификацию `Agent Builder` включить универсальные правила:
  - где лежит agent spec
  - где лежат integration notes / stub notes
  - где лежат scripts, если они нужны
  - как называются основные файлы
  - какой минимум должен быть у каждого агента, чтобы он считался complete
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: focused agent catalog
- Observation: для урока полезно временно ограничить каталог создания агентов четырьмя понятными сценариями вместо слишком широкого выбора.
- Impact: это снижает когнитивную нагрузку и даёт шанс довести этап до результата внутри занятия.
- Proposed change: базовый каталог этапа `create/adapt agent` ограничить такими вариантами:
  - Telegram Digest Agent
  - Review Monitor Agent
  - Notion Sync Agent
  - Resume Analysis Agent
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: scenario-specific guidance
- Observation: для каждого из четырёх сценариев нужен не просто шаблон агента, а пошаговый guide: какие данные нужны, что можно подключить, что можно заменить экспортом или заглушкой, и как получить первый рабочий результат.
- Impact: иначе участник выберет сценарий, но застрянет на вопросе "и что теперь конкретно делать?".
- Proposed change: `Agent Builder` должен уметь по каждому сценарию:
  - объяснить, какие входные данные нужны
  - запросить недостающий контекст
  - предложить самый простой путь запуска
  - если нужна интеграция, дать guide по подключению или safe fallback
  - собрать минимально рабочий первый вариант агента
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: resume analysis requirements
- Observation: для сценария анализа резюме нужен отдельный обязательный контекст компании и вакансии; без него агент будет слишком абстрактным.
- Impact: результат может выглядеть как generic summary резюме без реальной пользы для HR.
- Proposed change: для `Resume Analysis Agent` `Agent Builder` должен обязательно запрашивать:
  - описание роли / вакансии
  - критерии отбора
  - формат входа (одно резюме или пакет)
  - ожидаемый результат анализа
  - где человек принимает финальное решение
- Priority: high
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: implementation realism
- Observation: если участник хочет не только описать агента, но и получить что-то, чем можно пользоваться дальше, `Agent Builder` должен уметь предлагать не только markdown-spec, но и минимальный каркас реализации там, где это оправдано.
- Impact: это усиливает ощущение реалистичности и переносимости результата после урока.
- Proposed change: предусмотреть двухуровневый output:
  - обязательный: agent spec + optional integration/stub notes
  - опциональный: scripts/config placeholders/minimal run instructions
  при этом опциональный технический слой не должен блокировать завершение урока
- Priority: medium
- Status: captured

### 2026-04-02 14:XX (captured)
- Stage: telegram agent narrowing
- Observation: `Telegram Digest Agent` нужно сузить до двух понятных способов получения входа:
  - выгрузка чата
  - подключение к Telegram-группе / каналу
- Impact: без такой развилки сценарий слишком расплывчатый и участнику непонятно, как именно начать.
- Proposed change: в guide для этого агента явно описать:
  - какие два пути доступны
  - как сырые данные попадают в общую структуру хранения
  - что этот агент готовит raw input bundle для дальнейшей обработки основной цепочкой агентов
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: notion sync positioning refinement
- Observation: `Notion Sync Agent` должен ориентироваться на уже сформированные выходные данные цепочки: задачи, описание проекта и связанные итоговые артефакты.
- Impact: так его роль становится понятной: он не собирает сырьё, а раскладывает готовый результат в систему.
- Proposed change: для этого агента зафиксировать:
  - что он принимает на вход итоговые данные после основной обработки
  - что он раскладывает задачи и описание проекта в целевую структуру
  - что нужно отдельно определить: MCP или API integration path и соответствующий guide
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: resume analysis refinement
- Observation: для анализа резюме нужен не только контекст компании, но и реестр вакансий с критериями по каждой вакансии; обработка должна идти не "вообще", а относительно выбранной вакансии.
- Impact: без привязки к вакансии анализ становится слишком общим и мало полезным.
- Proposed change: для `Resume Analysis Agent` зафиксировать:
  - обязательный контекст компании
  - реестр вакансий
  - критерии по выбранной вакансии
  - способ загрузки одного или нескольких резюме
  - анализ пачки резюме только в контексте конкретной вакансии
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: review monitor narrowing
- Observation: `Review Monitor Agent` тоже нужно сузить по источникам и path получения данных, а не оставлять как абстрактный "анализ отзывов".
- Impact: без ограничения по площадкам и способу доступа сценарий остаётся слишком расплывчатым.
- Proposed change: определить для него ограниченный набор площадок / источников и для каждой:
  - возможный способ получения данных
  - нужно ли подключение внешнего инструмента или MCP
  - как сырые данные складываются в общую структуру хранения
  - как они затем передаются в основную цепочку анализа
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: elective agents integration into core chain
- Observation: по сути, Telegram, Review Monitor и похожие агенты должны поставлять сырые данные в основную цепочку агентов, а Notion Sync — работать с итоговыми данными на выходе.
- Impact: это даёт гораздо более ясную архитектурную логику, чем воспринимать каждый elective agent как изолированный мини-продукт.
- Proposed change: в lesson architecture явно разделить:
  - агенты, которые подают сырьё в core chain
  - core chain, которая превращает сырьё в рабочий результат
  - агент, который раскладывает итог в систему на выходе
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: validation layer structure
- Observation: текущий validation layer оформлен как набор файлов в `validators/` и `evals/`, но не описан как явный dispatchable workflow или как отдельный orchestrator-agent, который участник может легко вызвать одной командой.
- Impact: участнику и помощнику неочевидно, что именно должно запускаться на intent `валидируй` или `проверь моего агента`, и как соотносятся `validators/*` с `agents/*`.
- Proposed change: оформить validation layer явнее:
  - либо как `Validation Orchestrator` + набор validator-agents/specs
  - либо как явный `validation workflow`, который диспетчеризация умеет запускать по participant intent
  при этом в participant-facing UX запуск остаётся одной простой командой.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: validation scope expansion
- Observation: текущие валидаторы покрывают старую модель agent design, но уже не покрывают новые требования, которые мы проектируем для agent builder, dispatch layer, file layout и handoff artifacts.
- Impact: validation может давать формально "хороший" verdict для агента, который не соответствует новой архитектуре урока.
- Proposed change: при доработке validation layer добавить проверки на:
  - соответствие canonical file layout
  - наличие required artifacts
  - соответствие dispatch conventions
  - корректность handoff pattern
  - понятный integration/fallback guide
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: consistency principles for validation
- Observation: чтобы не получилась "каша", нужно единообразие не только в содержании, но и в том, как validation layer выглядит для пользователя и для репозитория.
- Impact: если validation будет оформлен совсем иначе, чем остальные agent workflows, participant experience станет ломким и непредсказуемым.
- Proposed change: зафиксировать единые принципы:
  - рабочие агенты лежат в `agents/`
  - проверяющие агенты лежат в `validators/`
  - оба слоя используют похожую структуру spec-файлов (`Role`, `Inputs/Check`, `Output`, `Guardrails`)
  - dispatch layer умеет запускать и рабочие шаги, и validation intents
  - для участника и то, и другое вызывается короткой командой
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: validation best-practice pattern
- Observation: validation лучше проектировать не как одного "всезнающего" валидатора, а как оркестратор плюс несколько узких reviewer-агентов.
- Impact: это даёт более ясные границы ответственности, легче расширяется и лучше соответствует общей multi-agent логике урока.
- Proposed change: принять recommended pattern:
  - `Validation Orchestrator` принимает participant intent `валидируй` / `проверь моего агента`
  - он запускает `agent curator`, `safety validator`, `architecture validator`, `skill curator`
  - собирает их outputs
  - затем `eval orchestrator` выдаёт единый `validation_report`
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: participant-facing validation command
- Observation: запуск validation для участника должен быть одной простой фразой, а не требовать знания внутренней структуры `validators/*`.
- Impact: иначе этап validation будет восприниматься как технический аудит, а не как естественное продолжение create/adapt flow.
- Proposed change: в dispatch layer добавить явный action наподобие:
  - `проверь моего агента`
  - `запусти валидацию`
  который под капотом запускает весь validation workflow и сохраняет `validation_report`.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: validation orchestrator draft
- Observation: для нового validation UX нужна явная внутренняя роль, которая оркестрирует запуск валидаторов и собирает единый результат.
- Impact: без этого participant-facing команда останется красивой оболочкой без ясно описанного внутреннего механизма.
- Proposed change: ввести `Validation Orchestrator` со следующей логикой:
  - принимает intent `проверь моего агента` / `запусти валидацию`
  - определяет текущий agent spec и связанные артефакты
  - запускает `agent curator`, `skill curator`, `safety validator`, `architecture validator`
  - передаёт результаты в `eval orchestrator`
  - сохраняет единый `validation_report`
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: participant-facing validation phrasing
- Observation: участнику нужен короткий и естественный вход в validation stage без технических деталей.
- Impact: если phrasing будет слишком техническим, этап будет восприниматься как отдельная сложная процедура.
- Proposed change: использовать participant-facing формулировку:
  - `Проверь моего агента и сделай validation report.`
  или
  - `Запусти валидацию моего агента и покажи, что нужно исправить.`
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: personal next step trigger
- Observation: финальный этап `personal next step` тоже должен иметь понятный participant-facing trigger и не должен выглядеть как неформальный разговор "ну а теперь подумай сам".
- Impact: без явного запуска и структуры финал урока может расплыться и не привести к конкретному следующему действию.
- Proposed change: оформить этот этап как явный workflow с participant-facing командой, например:
  - `Помоги мне определить мой следующий шаг`
  - `Давай сформулируем мой personal next step`
  и с внутренней логикой, которая опирается на `personal_next_step_template.md` и `final_action_card_template.md`.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: personal next step UX
- Observation: участнику нужно не просто заполнить шаблон, а пройти короткий guided reflection с вопросами по одному, чтобы на выходе получился качественный и реалистичный результат.
- Impact: если дать только шаблон, участник может уйти в абстракцию или слишком широкий сценарий.
- Proposed change: personal next step stage должен работать так:
  - участник запускает этап короткой командой
  - помощник задаёт короткие вопросы по одному
  - ответы складываются в `personal_next_step.md`
  - затем из этого формируется `final_action_card.md`
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: migration plan to skills
- Observation: текущий runtime layer репозитория оформлен как набор markdown-описаний в `agents/` и `validators/`, но по документации Codex reusable workflows каноничнее оформлять как skills в `.agents/skills/`.
- Impact: без миграции в канонический формат repo хуже соответствует best practices Codex и сложнее масштабируется как набор переиспользуемых workflow.
- Proposed change: принять migration-first plan и начать доработку репозитория именно с миграции существующего слоя в skills.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: migration order
- Observation: миграцию нужно делать поэтапно, сохраняя педагогическую структуру урока и не ломая текущий материал.
- Impact: если пытаться одновременно мигрировать всё и перепридумывать lesson flow, получится слишком много изменений сразу.
- Proposed change: порядок работ:
  1. определить каноническую skill-структуру в `.agents/skills/`
  2. перенести текущие core workflow steps в skills
  3. перенести validation в отдельный skill/workflow
  4. перенести финальный personal-next-step в skill
  5. только потом проектировать новые skills (`task-register`, `agent-builder`, новые elective scenarios)
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: v1 migration scope
- Observation: для первой миграции не нужно переносить абсолютно всё; достаточно перенести минимальный рабочий набор, который соответствует реальному lesson flow.
- Impact: это позволяет быстро получить канонический каркас Codex без расползания объёма.
- Proposed change: `v1` migration scope:
  - `shared-case-intake`
  - `shared-case-analysis`
  - `shared-case-workflow`
  - `shared-case-experiment`
  - `validate-agent`
  - `personal-next-step`
  при этом текущие `agents/core/*`, `validators/*`, `participants/templates/*` можно временно использовать как source material / references during migration.
- Priority: high
- Status: implemented

### 2026-04-02 14:XX (captured)
- Stage: post-migration roadmap
- Observation: после миграции базового lesson flow в skills можно уже безопасно достраивать улучшения, которые мы наобсуждали.
- Impact: это даёт правильную последовательность работ и снижает риск строить новые слои на неканоничном фундаменте.
- Proposed change: после завершения migration-first слоя двигаться в таком порядке:
  1. `task-register` skill
  2. `agent-builder` skill
  3. обновлённый dispatch layer
  4. доработка validation criteria
  5. новые elective scenarios (`resume analysis`, refined `telegram`, refined `review monitor`, refined `notion sync`)
- Priority: high
- Status: partial

### 2026-04-02 14:XX (captured)
- Stage: hybrid validation architecture
- Observation: validation layer в Codex логичнее строить не только на skills и не как набор независимых subagents, а как один custom orchestrator agent, который использует несколько validation skills последовательно.
- Impact: это даёт простой participant UX (`Проверь мой skill`), сохраняет модульность проверок и не создаёт лишний orchestration overhead для воркшопа.
- Proposed change: принять hybrid validation model:
  - `.codex/agents/validation-orchestrator.toml` как entrypoint
  - `.agents/skills/reviewer-role/`
  - `.agents/skills/safety-validator/`
  - `.agents/skills/architecture-validator/`
  - при необходимости `.agents/skills/skill-structure-check/`
  - итоговый verdict и `validation_report` собираются в `validation-orchestrator`
- Priority: high
- Status: implemented
