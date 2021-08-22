QUERY_V1 = """
 query QueryLanguageV1(
    $query: String!
    $variables: JSON
    $includeDeleted: Boolean
    $deferredResponse: DeferredResponseOption
    $deferredFormat: DeferredResponseFormat
  ) {
    queryV1(
      query: $query
      variables: $variables
      includeDeleted: $includeDeleted
      deferredResponse: $deferredResponse
      deferredFormat: $deferredFormat
    ) {
      type
      data
      url
    }
  }
"""

CREATE_ENTITY = """
  mutation CreateEntity(
    $entityKey: String!
    $entityType: String!
    $entityClass: [String!]!
    $properties: JSON
  ) {
    createEntity(
      entityKey: $entityKey
      entityType: $entityType
      entityClass: $entityClass
      properties: $properties
    ) {
      entity {
        _id
      }
      vertex {
        id
        entity {
          _id
        }
      }
    }
  }
"""

DELETE_ENTITY = """
  mutation DeleteEntity(
    $entityId: String!,
    $timestamp: Long
    $hardDelete: Boolean
    ) {
    deleteEntity(
      entityId: $entityId,
      timestamp: $timestamp
      $hardDelete: $hardDelete
    ) {
      entity {
        _id
        _deleted
        _endOn
      }
      vertex {
        id
        properties
      }
    }
  }
"""

UPDATE_ENTITY = """
  mutation UpdateEntity($entityId: String!, $properties: JSON) {
    updateEntity(entityId: $entityId, properties: $properties) {
      entity {
        _id
      }
      vertex {
        id
      }
    }
  }
"""

CREATE_RELATIONSHIP = """
  mutation CreateRelationship(
    $relationshipKey: String!
    $relationshipType: String!
    $relationshipClass: String!
    $fromEntityId: String!
    $toEntityId: String!
    $properties: JSON
  ) {
    createRelationship(
      relationshipKey: $relationshipKey
      relationshipType: $relationshipType
      relationshipClass: $relationshipClass
      fromEntityId: $fromEntityId
      toEntityId: $toEntityId
      properties: $properties
    ) {
      relationship {
        _id
      }
      edge {
        id
        toVertexId
        fromVertexId
        relationship {
          _id
        }
        properties
      }
    }
  }
"""

DELETE_RELATIONSHIP = """
  mutation DeleteRelationship($relationshipId: String! $timestamp: Long) {
    deleteRelationship (relationshipId: $relationshipId, timestamp: $timestamp) {
      relationship {
        _id
      }
      edge {
        id
        toVertexId
        fromVertexId
        relationship {
          _id
        }
        properties
      }
    }
  }
"""

UPSERT_ENTITY_RAW_DATA = """
  mutation UpsertEntityRawData(
    $entityId: String!
    $source: String!
    $rawData: [JSON!]!
  ) {
    upsertEntityRawData(
      entityId: $entityId
      source: $source
      rawData: $rawData
    ) {
      status
    }
  }
"""

CREATE_ALERT_RULE = """
  mutation CreateQuestionRuleInstance(
    $instance: CreateQuestionRuleInstanceInput!
  ) {
    createQuestionRuleInstance(instance: $instance) {
      id
      name
    }
  }
"""

UPDATE_ALERT_RULE = """
  mutation UpdateQuestionRuleInstance(
    $instance: UpdateQuestionRuleInstanceInput!
  ) {
    updateQuestionRuleInstance(instance: $instance) {
      id
      name
      description
      version
      specVersion
      latest
      deleted
      pollingInterval
      templates
      question {
        queries {
          name
          query
          version
        }
      }
      operations {
        when
        actions
      }
      outputs
    }
  }
"""

CREATE_QUESTION = """
  mutation CreateQuestion($question: CreateQuestionInput!) {
    createQuestion(question: $question) {
      id
      title
      description
      queries {
        query
        version
      }
      variables {
        name
        required
        default
      }
      compliance {
        standard
        requirements
      }
      tags
      accountId
      integrationDefinitionId
    }
  }
"""


UPDATE_QUESTION = """
  mutation UpdateQuestion($id: ID!, $update: QuestionUpdate!) {
    updateQuestion(id: $id, update: $update) {
      id
      title
      description
      queries {
        query
        version
      }
      variables {
        name
        required
        default
      }
      compliance {
        standard
        requirements
      }
      tags
      accountId
      integrationDefinitionId
    }
  }
"""

DELETE_QUESTION = """
  mutation DeleteQuestion($id: ID!) {
    deleteQuestion(id: $id) {
      id
      title
      description
      queries {
        query
        version
      }
      variables {
        name
        required
        default
      }
      compliance {
        standard
        requirements
      }
      tags
      accountId
      integrationDefinitionId
    }
  }
"""
