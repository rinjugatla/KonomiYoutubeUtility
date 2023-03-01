<script>
	import Chapters from './Chapters.svelte';

	export let live;
	let date = '1999-09-09';
	let chapter_count = 0;
	$: {
		date = live.date_published.substring(0, 10);
		chapter_count = live.chapters.length;
	}
</script>

<div class="ui center aligned" style="margin-top:4em;">
	<div class="ui card">
		<div class="image">
			<img src={live.thumbnail} alt={live.title} />
		</div>
		<div class="content">
			<a class="header" href={live.url} target="_blank" rel="noopener noreferrer">{live.title}</a>
			<div class="meta">
				<span class="date">{date}</span>
			</div>
			<div class="description">
				<Chapters chapters={live.chapters} />
			</div>
		</div>
		<div class="extra content">
			<i class="music icon" />
			{chapter_count} Chapters
		</div>
	</div>
</div>
