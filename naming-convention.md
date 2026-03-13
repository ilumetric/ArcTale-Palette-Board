## Общие принципы

Название файлов и путь их расположения в проекте выдаётся вместе с техническим заданием.

В именах не используются пробелы, тире и дефисы, только нижние подчёркивания. Индексация обязательна с первой версии ассета: `_01`, `_02`, `_03` и так далее.

В проекте используется принцип двух папок: структура размещения ассета в контенте и имя самого ассета должны быть согласованы между собой. Имя ресурса должно отражать директорию, к которой он относится, и собственное имя объекта.

Например, если ассет лежит в папке `Content\Ansora\Art\Environment\DepotProps\Art`, то имя должно собираться по схеме с названием директории и названием ассета, например: `SM_DepotProps_Art_Paintings_01`.

## Правила именования ассетов

### Префиксы

| Тип ассета | Префикс | Пример |
| --- | --- | --- |
| Static Mesh | `SM_` | `SM_DepotProps_Paintings_01` |
| Master Material | `MM_` | `MM_Glass_01` |
| Material | `M_` | `M_Glass_01` |
| Texture | `T_` | `T_DepotProps_Paintings_D_01` |

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

Тип текстуры указывается перед индексом. Это обновлённое правило: в старой схеме порядок типа и индекса мог отличаться.

#### Типы текстур

| Обозначение | Назначение |
| --- | --- |
| `D` | Base Color |
| `ORM` | AO / Roughness / Metallic |
| `N` | Normal |
| `M`, `M1`, `M2` | Mask |
