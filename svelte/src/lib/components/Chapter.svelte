<script>
	export let chapter;
</script>

<div class="item">
	<div class="content">
		<a href={chapter.url} target="_blank" rel="noopener noreferrer">
			<div class="header">{chapter.title}</div>
		</a>
		{chapter.artists ?? ''}
	</div>
</div>
