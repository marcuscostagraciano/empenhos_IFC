<script setup>
const props = defineProps(['value', 'label']);

const formattedValue = new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL'
}).format(props.value);

</script>

<template>
    <h4 class="text-h4 font-weight-bold" :class="{'text-red' : value < 0}">
        {{ formattedValue }}
    </h4>
    <h6 class="pt-4 text-subtitle-2 text-grey font-italic">
        {{ label }}
    </h6>
</template>