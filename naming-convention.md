## Общие принципы

Имя файла и путь в проекте выдаются вместе с ТЗ.

Пробелы, тире и дефисы не используются, только нижнее подчёркивание. Индекс обязателен с первой версии: `_01`, `_02`, `_03`.

Путь и имя ассета согласованы: имя повторяет директорию и собственное имя объекта. Ассет из `Content\ArcProject\Art\Environments\DepotProps\Art` называется `SM_DepotProps_Art_Paintings_01`.

Папки называются в единственном числе: `Frame`, `Floor`, `Socket`, `Base`. Причины:

- **Единообразие.** Множественное число ломается на неисчисляемых и неправильных словах (`Glass`, `Foliage`, `Shelves`). Единственное число всегда работает.
- **Совпадает с префиксом/именем ассета.** `SM_Train_Frame_01` лежит в `Train/Frame`, путь читается как одно имя.
- **Так делает Epic.** В официальных гайдах (Allar's Style Guide, Lyra, стартовые проекты) папки называются `Character`, `Weapon`, `Prop`, `Environment`, а не во множественном.

## Правила именования ассетов

### Префиксы

| Тип ассета | Префикс | Пример |
| --- | --- | --- |
| Static Mesh | `SM_` | `SM_DepotProps_Paintings_01` |
| Skeletal Mesh | `SKM_` | `SKM_Vegetation_PineTree_01` |
| Skeleton | `SKEL_` | `SKEL_Vegetation_PineTree_01` |
| Physics Asset | `PHYS_` | `PHYS_Vegetation_PineTree_01` |
| Master Material | `MM_` | `MM_Glass_01` |
| Material | `M_` | `M_Glass_01` |
| Material Instance | `MI_` | `MI_Glass_Frosted_01` |
| Texture | `T_` | `T_DepotProps_Paintings_D_01` |
| PVE Graph | `PVE_` | `PVE_Train_Door_01` |

### Static Mesh

Формат имени:

`SM_<DirectoryName>_<AssetName>_<Index>`

Примеры:

- `SM_DepotProps_Art_Paintings_01`
- `SM_Train_ArtifactFigurines_01`

### Texture

Формат имени:

`T_<DirectoryName>_<AssetName>_<TextureType>_<Index>`

Примеры:

- `T_DepotProps_Paintings_D_01`
- `T_DepotProps_Paintings_ORM_01`
- `T_DepotProps_Paintings_N_01`
- `T_DepotProps_Paintings_M_01`

Тип текстуры стоит перед индексом.

#### Типы текстур

| Обозначение | Назначение |
| --- | --- |
| `D` | Base Color |
| `ORM` | AO / Roughness / Metallic |
| `N` | Normal |
| `M`, `M1`, `M2` | Mask |
