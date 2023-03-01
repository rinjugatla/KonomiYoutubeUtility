<script>
	import YoutubeLive from './YoutubeLive.svelte';

	export let lives;
</script>

<div class="ui equal width center aligned padded grid">
	{#each lives as live}
		<YoutubeLive {live} />
	{/each}
</div>
