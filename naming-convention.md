## Общие принципы

::: card Базовые правила
- Имя файла и путь в проекте выдаются вместе с ТЗ.
- Разделитель только нижнее подчёркивание. Пробелы, тире и дефисы запрещены.
- Индекс обязателен с первой версии: `_01`, `_02`, `_03`.
:::

::: card Имя повторяет путь
Путь в контенте и имя ассета согласованы: имя собирается из директории и собственного имени объекта.

`Content\ArcProject\Art\Environments\DepotProps\Art` → `SM_DepotProps_Art_Paintings_01`
:::

::: card Папки в единственном числе | Правило
- (+) `Frame`, `Floor`, `Socket`, `Base`
- (-) `Frames`, `Floors`, `Sockets`, `Bases`

---

- **Единообразие.** Множественное число ломается на неисчисляемых и неправильных словах: `Glass`, `Foliage`, `Shelves`. Единственное число работает всегда.
- **Совпадает с именем ассета.** `SM_Train_Frame_01` лежит в `Train/Frame`, путь читается как одно имя.
- **Так делает Epic.** В Allar's Style Guide, Lyra и стартовых проектах папки называются `Character`, `Weapon`, `Prop`, `Environment`.
:::

## Префиксы

::: card Геометрия и ассеты
- `SM_` Static Mesh — `SM_DepotProps_Paintings_01`
- `SKM_` Skeletal Mesh — `SKM_Vegetation_PineTree_01`
- `SKEL_` Skeleton — `SKEL_Vegetation_PineTree_01`
- `PHYS_` Physics Asset — `PHYS_Vegetation_PineTree_01`
:::

::: card Материалы
- `MM_` Master Material — `MM_Glass_01`
- `M_` Material — `M_Glass_01`
- `MI_` Material Instance — `MI_Glass_Frosted_01`
:::

::: card Текстуры и графы
- `T_` Texture — `T_DepotProps_Paintings_D_01`
- `PVE_` PVE Graph — `PVE_Vegetation_PineTree_01`
:::

## Шаблоны имён

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

::: card Типы текстур
- `D` Base Color
- `ORM` AO / Roughness / Metallic
- `N` Normal
- `M`, `M1`, `M2` Mask
:::
