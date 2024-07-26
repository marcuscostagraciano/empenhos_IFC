<template>
  <header class="mx-16 mt-16 border-b-thin pb-2">
    <h1 class="text-h3 font-weight-bold">
      Painel de Transparência Financeira do
      <span class="text-green-darken-3">IFC - Campus Araquari</span>
    </h1>
    <!-- <p class="pb-4 pt-2 text-primary">Version {{ version }}</p> -->
    <p class="py-6 text-grey">
      Este projeto tem por objetivo possibilitar à comunidade o acompanhamento
      da execução do orçamento do campus. As informações são apresentadas
      considerando, ao longo do tempo, os valores de Despesas Empenhadas e
      Despesas Liquidadas.
    </p>
    <v-row>
      <v-col cols="12" lg="3" sm="6">
        <v-autocomplete
          v-model="state"
          :items="['Santa Catarina', '...']"
          label="Selecione o Estado"
          variant="outlined"
        />
      </v-col>
      <v-col cols="12" lg="3" sm="6">
        <v-autocomplete
          v-model="school"
          :items="['Araquari', '...']"
          label="Selecione o Campus"
          variant="outlined"
        />
      </v-col>
    </v-row>
  </header>
</template>

<script lang="ts" setup>
  // const version = '1.0.5'
  const school = ref<string[]>(['Araquari'])
  const state = ref<string[]>(['Santa Catarina'])
</script>
