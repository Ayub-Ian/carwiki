import React from "react";

import Link from "next/link";
import Image from "next/image";
import CountdownTimer from "./CountdownTimer";

export default function AuctionCard({ auction }) {
  return (
    <Link href={`/auctions/details/${auction.id}`} className="group">
      <div className="bg-white dark:bg-white/10 p-6 rounded-lg">
        <div className="flex flex-col  items-start mb-4">
          <h3 className="font-semibold text-xl">
            {auction.make} {auction.model}
          </h3>
          <div className="flex items-center gap-1 text-gray-400">
            <p className="font-semibold text-sm ">{auction.year}</p>
            <div className="h-1 w-1 rounded-full bg-gray-400"></div>
            <p className="font-semibold text-sm ">{auction.mileage}km</p>
          </div>
        </div>
        <div className="w-full h-56 bg-gray-200 aspect-w-16 relative aspect-h-10 rounded-lg overflow-hidden">
          <div className=" h-full">
            <Image
              src={auction.imageUrl}
              alt="image"
              fill
              priority
              className={`
                object-cover
                group-hover:opacity-75
                duration-700
                ease-in-out
                
            `}
              sizes="(max-width:768px) 100vw, (max-width: 1200px) 50vw, 25vw"
            />
          </div>
        </div>

        <div className="flex items-center mt-4 justify-between">
          <div className="flex flex-col">
            <span className="text-sm font-medium text-gray-400">
              Reserve price
            </span>
            <h3 className="font-bold text-xl">Kes {auction.reservePrice}</h3>
          </div>
          <div>
            <CountdownTimer auctionEnd={auction.auctionEnd} />
          </div>
        </div>
      </div>
    </Link>
  );
}
