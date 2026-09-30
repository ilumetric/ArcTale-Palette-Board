## Общие принципы {#principles}

::: card Базовые правила {#base-rules}
- Имя файла и путь в проекте выдаются вместе с ТЗ.
- Разделитель только нижнее подчёркивание. Пробелы, тире и дефисы запрещены.
- Индекс обязателен с первой версии: `_01`, `_02`, `_03`.
:::

::: card Имя повторяет путь {#name-from-path}
Путь в контенте и имя ассета согласованы: имя собирается из директории и собственного имени объекта.

`Content\ArcProject\Art\Environments\DepotProps\Art` → `SM_DepotProps_Art_Paintings_01`

Структура папок и правила их именования описаны в разделе [Directories](#directories).
:::

## Префиксы {#prefixes}

::: card Геометрия и физика {#mesh-prefixes}
- `SM_` Static Mesh — `SM_DepotProps_Paintings_01`
- `SKM_` Skeletal Mesh — `SKM_Vegetation_PineTree_01`
- `PHYS_` Physics Asset — `PHYS_Vegetation_PineTree_01`
- `PM_` Physical Material — `PM_Metal_01`
:::

::: card Материалы {#material-prefixes}
- `MM_` Master Material — `MM_Glass_01`
- `M_` Material — `M_Glass_01`
- `MI_` Material Instance — `MI_Glass_Frosted_01`
- `PPM_` Post Process Material — `PPM_Outline_01`
:::

::: card Текстуры и графы {#texture-prefixes}
- `T_` Texture — `T_DepotProps_Paintings_D_01`
- `HDR_` HDRI — `HDR_Overcast_01`
- `PVE_` PVE Graph — `PVE_Vegetation_PineTree_01`
:::

::: card Анимация {#anim-prefixes}
- `SKEL_` Skeleton — `SKEL_Vegetation_PineTree_01`
- `Rig_` Control Rig
- `IK_` IK Rig — `IK_Character_Hero_01`
- `RTG_` IK Retargeter
- `AS_` Animation Sequence
- `AM_` Animation Montage
- `BS_` Blend Space
- `ABP_` Animation Blueprint
- `LS_` Level Sequence
- `EDIT_` Sequencer Edits
:::

::: card Блюпринты и данные {#blueprint-prefixes}
- `BP_` Blueprint
- `AC_` Actor Component
- `BI_` Blueprint Interface
- `WBP_` Widget Blueprint
- `DT_` Data Table
- `CT_` Curve Table
- `E_` Enum
- `F_` Structure
:::

::: card Эффекты {#fx-prefixes}
- `FXS_` Niagara System
- `FXE_` Niagara Emitter
- `FXF_` Niagara Function
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

::: card Static Mesh | SM_
`SM_<DirectoryName>_<AssetName>_<Index>`

Примеры

- `SM_DepotProps_Art_Paintings_01`
- `SM_Train_ArtifactFigurines_01`
:::

::: card Texture | T_
`T_<DirectoryName>_<AssetName>_<TextureType>_<Index>`

Примеры

- `T_DepotProps_Paintings_D_01`
- `T_DepotProps_Paintings_ORM_01`
- `T_DepotProps_Paintings_N_01`
- `T_DepotProps_Paintings_M_01`

> [!IMPORTANT]
> Тип текстуры стоит перед индексом.
:::

::: card Типы текстур {#texture-types}
- `D` Base Color
- `ORM` AO / Roughness / Metallic
- `N` Normal
- `M`, `M1`, `M2` Mask
:::
