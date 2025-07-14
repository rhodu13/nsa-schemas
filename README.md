# **NSA Schemas**

**`nsa-schemas`** est une librairie Python centralisée regroupant tous les schémas Pydantic utilisés dans l’écosystème NSA.

Elle permet de **partager un modèle de données cohérent entre les microservices**, notamment pour la gestion des équipes, des membres, des disponibilités et des plannings.

## **📦 Contenu de la librairie**

| Entité           | Schémas disponibles                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------------- |
| **Team**         | `TeamBase`, `TeamCreate`, `TeamUpdate`, `TeamOut`                                                        |
| **Member**       | `MemberBase`, `MemberCreate`, `MemberUpdate`, `MemberOut`                                                |
| **Availability** | `AvailabilityBase`, `AvailabilityCreate`, `AvailabilityUpdate`, `AvailabilityUpsert`, `AvailabilityInDB` |
| **Planning**     | `PlanningBase`, `PlanningCreate`, `PlanningUpdate`, `PlanningOut`                                        |

## **🚀 Installation**

### Mode développement (locale)

Si la librairie est dans le même repo ou à côté :

```bash
pip install -e .
```

Ou depuis un autre microservice :

```bash
pip install -e ../nsa-schemas
```

### Installation via `requirements.txt`

Ajoute dans ton `requirements.txt` :

```txt
-e ../nsa-schemas
```

## **🔧 Utilisation**

Dans n’importe quel microservice :

```python
from nsa_schemas import TeamCreate, MemberOut, AvailabilityInDB, PlanningOut
```

## **📂 Arborescence**

```
nsa-schemas/
├── nsa_schemas/
│   ├── __init__.py
│   ├── team.py
│   ├── member.py
│   ├── planning.py
│   └── availability.py
├── tests/
│   ├── test_team.py
│   ├── test_member.py
│   ├── test_planning.py
│   └── test_availability.py
├── pyproject.toml
├── README.md
└── pytest.ini
```

## **✅ Avantages**

* **Cohérence** des modèles de données entre les microservices
* **Séparation des responsabilités** (API vs Schémas)
* **Réutilisable et versionnable** (monorepo ou publication Git/PyPI)
* **100% compatible avec FastAPI, Pydantic v2 et SQLAlchemy**

## **🧪 Tests**

Lance les tests unitaires :

```bash
pytest
```

Génère un rapport de couverture :

```bash
pytest --cov=nsa_schemas --cov-report=html
```

Le rapport sera disponible dans `report.html`.

## **📈 Roadmap**

* ✅ Intégration des schémas `Teams`, `Members`, `Availabilities`, `Plannings`
* 🔜 Publication sur un registre Git ou PyPI privé
* 🔜 Génération automatique des OpenAPI schemas pour documentation externe

## **👨‍💻 Contributeurs**

* **@rhodu13** - Auteur principal
