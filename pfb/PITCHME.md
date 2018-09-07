# PFB

Portable Format for Biomedical Data

---

### Why do we want it
We need an efficient and neutral format to:
- Ship rich data across data commons
- Store previous versions of Commons' data

---

### Ship data across data commons
- We run ETL to transform our relational data to flat view, the ETL can also be external - a third-party Commons might want to use
our commons' data and represent in a different view. So we can give them PFB.
- This also works in another direction, we take over the data from another platform and require them to give us the data in PFB format, we trigger the async ETL job to import to our Commons.

---
### Store previous verions of Commons' data

Our Commons' rich data snapshot becomes PFB files instead of sqldump.
We can ETL a previous data snapshot to relational/graph/document database.

---

### PFB for async submission

1. gen3-data-client converts client data to PFB, do schema validation on client-side as pre-check.
2. Submit PFB data to Gen3 Commons asynchrounously.
3. PFB ETL to postgres.

---

### Serialization format
1. space efficient, fast serialization/deserialization.
2. good support working with big data frameworks.
3. support dynamic schema evolution so that importing data with new but compatible schema does not require software deployment

---

### Potential uses
1. The PFB schema will include ontology references, when two datasets use different terms but refers to the same ontology, we can ETL them to same field.
2. We can explore the possibility of using PFB data file as source of truth and postgres becomes a graph view

---
