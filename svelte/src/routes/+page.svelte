<script>
	import { onMount } from 'svelte';
	import YoutubeLives from '$lib/components/YoutubeLives.svelte';

	let lives;

	onMount(async () => {
		const res = await fetch('https://api.mofucloud.com/archive/videos');
		lives = await res.json();
	});
</script>

<svelte:head>
	<link
		rel="stylesheet"
		href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.5.0/semantic.min.css"
		integrity="sha512-KXol4x3sVoO+8ZsWPFI/r5KBVB/ssCGB5tsv2nVOKwLg33wTFP3fmnXa47FdSVIshVTgsYk/1734xSk9aFIa4A=="
		crossorigin="anonymous"
		referrerpolicy="no-referrer"
	/>
</svelte:head>

{#if lives}
	<YoutubeLives {lives} />
{:else}
	<p>Loading...</p>
{/if}
