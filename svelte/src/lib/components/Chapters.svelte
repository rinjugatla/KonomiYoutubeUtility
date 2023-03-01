<script>
	import Chapter from './Chapter.svelte';

	export let chapters;
</script>

<div class="ui segment">
	<div class="ui relaxed divided list">
		{#each chapters as chapter}
			<Chapter {chapter} />
		{/each}
	</div>
</div>
