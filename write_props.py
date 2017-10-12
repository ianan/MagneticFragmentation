
# coding: utf-8

# In[1]:

def write_props(props, polarity, image_num, image_date, submap):
    from astropy.coordinates import SkyCoord
    import astropy.units as u
    from sunpy.coordinates import frames

    # Create filename using the image_num and polarity
    filename = '/Users/fraser/Github/MagneticFragmentation/fragment_properties/'+'{0}'.format(image_date.strftime('%Y%m%d_%H%M%S'))+'_'+polarity+'.txt'

    # Open filename for writing
    f = open(filename, 'w')

    for region in props:
        # Check to see if the area of the fragment is 12 pixels or larger
        if region.area >= 12:
            # Get the pixel coordinates from the region.centroid and cast them as
            # pixels in astropy units. Then, use the sunpy submap to convert those
            # pixel coordinates to image coordinates (x-arcsecs and y-arcsecs)
            arcsecs_coord = submap.pixel_to_world(region.centroid[1] * u.pix,
                                                  region.centroid[0] * u.pix)
            # Now convert the coordinates to Heliographic latitude and longitude as
            # that is what we need to rotate coordinates in time later on
            latlong_coord = arcsecs_coord.transform_to(frames.HeliographicStonyhurst)
            # Record the area (area is NOT deprojected back onto the solar disk)
            area = region.area

            # Write the data to the file
            f.write('{0}, {1:6.1f}, {2:6.1f}, {3:5.0f}\n'.format(image_date,
                                                         latlong_coord.lat.value,
                                                         latlong_coord.lon.value,
                                                         area))
    # close the file
    f.close()

