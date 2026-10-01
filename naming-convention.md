## Общие принципы {#principles}

::: card Имя повторяет путь {#name-from-path} | Правило двух папок
Путь в контенте и имя ассета согласованы: имя собирается из **двух последних смысловых папок** пути и, если нужно, собственного имени объекта.

`Art\Prop\Depot\Generator` → `SM_Depot_Generator_Body_01`

`Art\Train\Frame` → `SM_Train_Frame_01`

`Art\Vegetation\Shared\Fern` → `SKM_Vegetation_Fern_01`

- Служебные папки не считаются: `Shared`, `Materials`, `Textures`, `Blueprints`, `Assemblies`.
- **Core** — исключение: папки в имя не входят, `MM_Glass_01`.
- **Ассемблы** растительности — исключение: `SM_Assembly_<Name>_<Index>`.

Структура папок — в [дереве на странице Directories](#directories/structure), правила именования папок — в [Directories](#directories/folder-naming).
:::

::: half Базовые правила {#base-rules}
- Имя файла и путь в проекте выдаются вместе с ТЗ.
- Разделитель только нижнее подчёркивание. Пробелы, тире и дефисы запрещены.
- Индекс обязателен с первой версии: `_01`, `_02`, `_03`.
:::

::: half Зачем две папки в имени {#why-two-folders}
Поиск в Content Browser идёт по имени ассета. Когда в имени есть префикс и папки, ассеты фильтруются сразу по типу и по месту: достаточно помнить, где лежит ассет, а не его точное имя.

- `MI_Depot` Все инстансы материалов из темы `Depot`
- `T_Depot_Generator` Все текстуры генератора
- `SM_Depot` Все меши из темы `Depot`

Одной папки мало: `Generator` может быть и в `Depot`, и в другой теме. Полный путь слишком длинный. Две папки однозначно указывают место и оставляют имя коротким.
:::

## Префиксы {#prefixes}

::: half Геометрия и физика {#mesh-prefixes}
- `SM_` Static Mesh — `SM_Depot_Generator_Body_01`
- `SKM_` Skeletal Mesh — `SKM_Vegetation_Fern_01`
- `PHYS_` Physics Asset — `PHYS_Vegetation_Fern_01`
- `PM_` Physical Material — `PM_Metal_01`
:::

::: half Материалы {#material-prefixes}
- `MM_` Master Material — `MM_Glass_01`
- `M_` Material — `M_Glass_01`
- `MI_` Material Instance — `MI_Glass_Frosted_01`
- `PPM_` Post Process Material — `PPM_Outline_01`
:::

::: half Текстуры и графы {#texture-prefixes}
- `T_` Texture — `T_Depot_Generator_Body_D_01`
- `HDR_` HDRI — `HDR_Overcast_01`
- `PVE_` PVE Graph — `PVE_Vegetation_Fern_01`
:::

::: half Эффекты {#fx-prefixes}
- `FXS_` Niagara System
- `FXE_` Niagara Emitter
- `FXF_` Niagara Function
:::

::: half Анимация {#anim-prefixes}
- `SKEL_` Skeleton — `SKEL_Vegetation_Fern_01`
- `Rig_` Control Rig
- `IK_` IK Rig — `IK_Human_Hero_01`
- `RTG_` IK Retargeter
- `AS_` Animation Sequence
- `AM_` Animation Montage
- `BS_` Blend Space
- `ABP_` Animation Blueprint
- `LS_` Level Sequence
- `EDIT_` Sequencer Edits
:::

::: half Блюпринты и данные {#blueprint-prefixes}
- `BP_` Blueprint
- `AC_` Actor Component
- `BI_` Blueprint Interface
- `WBP_` Widget Blueprint
- `DT_` Data Table
- `CT_` Curve Table
- `E_` Enum
- `F_` Structure
:::

::: card Медиа и прочее {#other-prefixes}
- `MS_` Media Source
- `MO_` Media Output
- `MP_` Media Player
- `MPR_` Media Profile
- `NDC_` nDisplay Configuration
- `OCIO_` OCIO Profile
- `SNAP_` Level Snapshots
- `RCP_` Remote Control Preset
:::

## Шаблоны имён {#templates}

::: half Static Mesh | SM_
`SM_<DirectoryName>_<AssetName>_<Index>`

Примеры

- `SM_Depot_Generator_Body_01`
- `SM_Train_Frame_01`
:::

::: half Texture | T_
`T_<DirectoryName>_<AssetName>_<TextureType>_<Index>`

Примеры

- `T_Depot_Generator_Body_D_01`
- `T_Depot_Generator_Body_ORM_01`
- `T_Depot_Generator_Body_N_01`
- `T_Depot_Generator_Body_M_01`

> [!IMPORTANT]
> Тип текстуры стоит перед индексом.
:::

::: card Типы текстур {#texture-types}
- `D` Base Color
- `ORM` AO / Roughness / Metallic
- `N` Normal
- `M`, `M1`, `M2` Mask
:::
