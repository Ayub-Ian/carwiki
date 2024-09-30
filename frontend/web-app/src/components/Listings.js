import AuctionCard from "@/modules/layout/components/AuctionCard"


async function getAuctions() {

    const res = await fetch("http://localhost:8000/search")

    if (!res) throw new Error('Failed to fetch data')

        return res.json()
    
}

export default async function AuctionListings() {
    const data = await getAuctions()

    console.log(data)
    return (
        <>
                            <div className='grid grid-cols-4 gap-6'>
                        {data.results.map(auction => (
                            <AuctionCard auction={auction} key={auction.id} />
                        ))}
                    </div>
        </>
    )
}