<script>
export default {
  name: 'smallButton',
  props: {
    Text: {
      type: String,
      required: true
    }
  }
}
</script>

<template>
  <div>
    <button>
      {{ Text }}
    </button>
  </div>
</template>
