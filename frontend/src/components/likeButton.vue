<script setup>
defineProps(['iconName'])
</script>

<template>
  <div class="backBtn">
    <button class="roundBtn">
      <svg
        width="32"
        height="32"
        viewBox="0 0 42 42"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M5.87729 4.86444C5.3709 5.25374 4.88708 5.69146 4.43146 6.17758C-0.143819 11.0591 -0.143819 18.9737 4.43146 23.8553L17.6863 37.9974C19.5164 39.95 22.4836 39.95 24.3137 37.9974L30.6226 31.2662M18.3985 4.08167C19.3311 4.63409 20.2081 5.33273 21 6.17758C25.5753 1.29603 32.9933 1.29603 37.5685 6.17758C42.1438 11.0591 42.1438 18.9737 37.5685 23.8553L37.25 24.1951"
          stroke="blue"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
        <path d="M2.25513 1L39.7455 41" stroke="blue" stroke-width="2" stroke-linecap="round" />
      </svg>
    </button>
    <button class="roundBtn">
      <svg width="32" height="32" viewBox="0 0 42 42" fill="red" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M37.5685 22.8767L22.4761 39.3854C21.6832 40.2527 20.3168 40.2527 19.5239 39.3854L4.43146 22.8767C-0.143819 17.8721 -0.143819 9.75806 4.43146 4.75345C9.00673 -0.251151 16.4247 -0.251151 21 4.75345C25.5753 -0.251151 32.9933 -0.251151 37.5685 4.75345C42.1438 9.75806 42.1438 17.8721 37.5685 22.8767Z"
          stroke="red"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </button>
  </div>
</template>

<style>
.backBtn {
  width: 100%;
  display: flex;
  margin-top: 10px;
  justify-content: center;
  align-items: center;
}
.roundBtn {
  justify-content: center;
  align-items: center;
  margin-left: 40px;
  margin-right: 40px;
  border-radius: 100%;
  width: 65px;
  height: 65px;
}
</style>
