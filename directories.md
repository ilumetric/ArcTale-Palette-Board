## Главное {#key-rules}

::: card Основная директория {#main-folder}
`Content/ArcProject/Art` — арт-ассеты. Папки верхнего уровня внутри `Art` создаются только по согласованию с лидом.
:::

::: half Shared + Theme {#shared-theme} | Правило
Общая схема для любого раздела, в том числе будущего:

- `Shared` Ассеты, которые используются в нескольких местах
- `<Theme>` Ассеты конкретной локации, набора, стиля или объекта

Ассет, который нужен только одной теме, лежит в ней, а не в `Shared`. Новый раздел строится по той же схеме. `Shared` в имя ассета не входит: `Vegetation/Shared/Fern` → `SKM_Vegetation_Fern_01`.
:::

::: half Из тестовой папки — в рабочую {#move-to-working} | Обязательно
После апрува **все** ассеты переносятся из личной тестовой папки в `Content/ArcProject/Art`: по структуре ниже и с именами по [Naming Convention](#naming).

После переноса тестовую папку нужно почистить. Как переносить — в разделе [Тестовая и рабочая папки](#directories/workflow).
:::

## Структура {#structure}

```tree groups
Content
  ArcProject
    Art
      Core — общий тех-арт, ни от кого не зависит
        Blueprints
        Materials — мастер-материалы, функции, инстансы
        Textures — маски, шумы, градиенты
      Characters — всё, что так или иначе персонажка
        Human — люди
          <Name> — ключевой персонаж
          Other — второстепенные: Other/<Name>
          Shared — общий риг, скелет, анимации людей
        Creature — существа: Creature/<Name>
          Shared
      Environments
        Shared — общее окружение: террейн, вода, небо
          ConcreteModule — модульный набор
        <Theme> — окружение конкретной локации
      Vegetation — растительность
        Shared — общая растительность
          Fern — пример: папка растения
            Assemblies — ассемблы и граф PVE
              SM_Assembly_Fern_01
              SM_Assembly_Fern_02
              PVE_Vegetation_Fern_01
            Materials
              MI_Vegetation_Fern_01
            SKM_Vegetation_Fern_01
            SKEL_Vegetation_Fern_01
            PHYS_Vegetation_Fern_01
        <Theme> — растительность конкретной локации
      Props — мелкие и средние объекты
        Shared — общие пропсы
        <Theme> — набор простых объектов по теме
      Train
        Base
        Frame — фреймы и меш сокета: SM_Train_Frame_Socket_01
        Sheathing — обшивка по стилям
          Default — Cabin, Floor, Wall, Roof: SM_Sheathing_Default_Cabin_01
          <Style> — стиль, если он тянет больше одного меша
        Ram? — тараны
        Module? — модули по подпапкам
      Weapon? — оружие
        Shared? — общие атачменты по классу: Attachment/Scope
        <Name>?
      Vehicle? — транспорт, как Train
```

> [!NOTE] Множественное число
> `Characters`, `Environments`, `Props` созданы по старому правилу. Новые папки называются в единственном числе. `Ram`, `Module`, `Weapon` и `Vehicle` пока не созданы — появятся вместе с контентом.

::: half Characters {#characters}
Всё, что так или иначе персонажка, лежит здесь, а не в корне: MetaHuman, скелетал меши, скелеты, анимации. Люди — в `Human/<Name>`, второстепенные — в `Human/Other`, общий риг людей — в `Human/Shared`. Существа от зверей до боссов — в `Creature/<Name>`.
:::

::: half Environments {#environments}
Аутдоры, здания, модульные наборы. Общее окружение — в `Shared`, окружение конкретной локации — в её теме. Модульный набор — своя папка: `Shared/ConcreteModule`.
:::

::: half Vegetation {#vegetation}
Каждое растение — своя папка: `Vegetation/Shared/<Name>` или `Vegetation/<Theme>/<Name>`.

- В папке растения — `SKM_`, `SKEL_`, `PHYS_`.
- `Materials` — материалы растения.
- `Assemblies` — все ассемблы и граф `PVE_` (Procedural Vegetation Editor).

Ассемблы не наследуют имя от пути: `SM_Assembly_<Name>_<Index>`.
:::

::: half Props {#props}
Мелкие и средние объекты. Общие — в `Shared`, остальные — по теме, а не по геймплейной функции: разрушаемость и интерактивность решает блюпринт, не папка.
:::

::: half Train {#train}
`Base` и `Frame` — основа. Обшивка — `Sheathing/<Style>`: пол, стены, кабины, крыши и декор-модули на стены, если стиль сдаётся паком. Стиль получает свою папку, только если тянет больше одного меша, иначе — в `Default`. Светильники и другие модули от стиля — в папке стиля. Меши стройки хаба вне поезда — в `Props`.
:::

::: half Weapon {#weapon}
Атачмент, общий для класса оружия, — в `Weapon/Shared/Attachment`. Уникальный для одной пушки — внутри её папки.
:::

## Типовые папки {#typed-folders}

::: card Materials и Textures {#materials-textures}
Типовые папки — `Materials` и `Textures`, для растительности ещё `Assemblies`. `Textures` лежит внутри `Materials`. Меши лежат прямо в папке объекта, папка `Meshes` не создаётся.

- Типовые папки — во множественном числе, так они отличаются от смысловых.
- В имя ассета типовые папки **не входят**, как и `Shared`. Все остальные папки — смысловые, в единственном числе, и в имя входят.
- **Исключение — `Core`:** там `Textures` на одном уровне с `Materials`, потому что текстуры Core работают во внешних материалах, а не только в мастер-материалах Core.
- **`Assemblies`** — типовая папка растительности, см. [Vegetation](#directories/vegetation).

```tree
Props
  Depot
    Generator
      Materials
        Textures
          T_Depot_Generator_Body_D_01
          T_Depot_Generator_Body_ORM_01
        MI_Depot_Generator_Body_01
      SM_Depot_Generator_Body_01
      SM_Depot_Generator_Panel_01
```
:::

## Принципы {#principles}

::: half Ассет лежит рядом с владельцем {#ownership}
Уникальный материал персонажа — в папке персонажа. Общий для всех людей — в `Characters/Human/Shared`. Общий для всего арта — в `Core`. Зависимости только вниз: объект берёт из `Core`, `Core` не зависит от объекта.
:::

::: half Своя папка — от двух мешей {#object-folder}
Объект получает свою папку, только если в нём больше одного меша: `Props/Depot/Generator` для корпуса и панели. Одиночный меш лежит прямо в папке темы: `Props/Depot/SM_Props_Depot_Lamp_01`.
:::

::: half Папка появляется вместе с контентом {#folder-with-content}
Пустые папки заранее не создаются. Для простого пропа не нужны свои `Materials`, если у него нет материалов. Глубина — не более пяти уровней после `Art`.
:::

::: half Нет глобальных папок по типу {#no-type-folders}
- (-) `Art/Meshes`, `Art/Textures`, `Art/Animations`

Ассет теряет принадлежность, файлы одного объекта разбросаны по проекту.
:::

::: half Нет папок-статусов {#no-status-folders}
- (-) `WIP`, `Review`, `Approved`, `Final`, `Old`, `Backup`, `Temp`, `New`

Статус живёт в трекере, а не в пути. Перемещение между такими папками плодит редиректоры.
:::

::: half В Art только визуал {#visual-only}
Блюпринты в `Art` только собирают или показывают визуальную часть объекта. Геймплейная логика хранится за пределами `Art`. Упаковка каналов в проекте одна — ORM.
:::

::: half Именование папок {#folder-naming}
- PascalCase, латиница: `WallLamp`, `MetalFence`. Без пробелов, дефисов и подчёркиваний.
- Смысловые папки — в единственном числе: `Frame`, `Floor`, `Socket`. Множественное ломается на `Glass`, `Foliage`, `Shelves`.
- Имя ассета повторяет путь: `Train/Frame` → `SM_Train_Frame_01`. Префиксы и шаблоны — в [Naming Convention](#naming).
:::

::: half Массовые переносы {#mass-moves}
Массовое перемещение и переименование — только по согласованию с лидом. После переноса проверить зависимости, карты и блюпринты, использующие ассеты, и запустить **Update Redirector References**.
:::

## Тестовая и рабочая папки {#workflow}

::: card После апрува {#after-approval}
- Пока ассет не прошёл апрув, он живёт в вашей личной тестовой папке.
- После апрува **все** ассеты переносятся в рабочую папку внутри `Content/ArcProject/Art` по структуре выше и получают имена по [Naming Convention](#naming).
- После переноса тестовую папку нужно почистить: копии, старые версии и неиспользуемые ассеты удаляются.

> [!WARNING] Переносить только через Content Browser
> Перемещайте ассеты в Content Browser, а не в проводнике, иначе сломаются ссылки. После переноса запустите на тестовой папке **Update Redirector References**.
:::

> [!IMPORTANT] Рабочие ассеты не ссылаются на тестовую папку
> Перед чисткой убедитесь, что ничего в `Content/ArcProject` не использует ассеты из вашей тестовой папки. Окно удаления в Unreal показывает найденные ссылки.
