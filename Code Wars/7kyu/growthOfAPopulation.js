/*
In a small town the population is p0 = 1000 at the beginning of the year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in town. How many years does the town need to see it's population greater or equal to p = 1200 inhabitants?
*/

const growthOfPopulation = (begins, percent, aug, populationSurpass) => {
	let currentPopulation = begins;
	let yearsPassed = 0;
	const realPercent = percent / 100;

	while (currentPopulation < populationSurpass) {
		currentPopulation = currentPopulation + (currentPopulation * realPercent) + aug;
		yearsPassed++;
	};

	return yearsPassed;
};
