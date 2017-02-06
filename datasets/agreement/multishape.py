from shapeworld.dataset import CaptionAgreementDataset
from shapeworld.generators.generic import GenericWorldGenerator
from shapeworld.captioners.dmrs.existential import ExistentialDmrsCaptioner


class MultiShapeDataset(CaptionAgreementDataset):

    def __init__(self, world_size, shapes, size_range, distortion_range, rotation, fills, colors, shade_range, noise_range, world_background_color, entity_counts, train_entity_counts, validation_entity_counts, test_entity_counts, caption_size, words, correct_ratio, train_correct_ratio, validation_correct_ratio, test_correct_ratio, **kwargs):
        super().__init__(
            world_generator=GenericWorldGenerator(world_size, shapes, size_range, distortion_range, rotation, fills, colors, shade_range, noise_range, world_background_color, entity_counts, train_entity_counts=train_entity_counts, validation_entity_counts=validation_entity_counts, test_entity_counts=test_entity_counts),
            world_captioner=ExistentialDmrsCaptioner(caption_size, words),
            incorrect_world_ratio=1.0,
            correct_ratio=correct_ratio,
            train_correct_ratio=correct_ratio,
            validation_correct_ratio=validation_correct_ratio,
            test_correct_ratio=test_correct_ratio)


dataset = MultiShapeDataset
MultiShapeDataset.default_config = {
    'world_size': [64, 64],
    'shapes': ['square', 'rectangle', 'triangle', 'pentagon', 'cross', 'circle', 'semicircle', 'ellipse'],
    'size_range': [0.1, 0.15],
    'distortion_range': [2.0, 3.0],
    'rotation': True,
    'fills': ['solid'],
    'colors': ['black', 'red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'white'],
    'shade_range': 0.5,
    'noise_range': 0.1,
    'world_background_color': 'black',
    'entity_counts': [1, 2, 3, 4, 5, 6],
    'train_entity_counts': [1, 2, 3, 4],
    'validation_entity_counts': [5],
    'test_entity_counts': [6],
    'caption_size': 6,
    'words': ['a', 'an', 'black', 'blue', 'circle', 'cross', 'cyan', 'ellipse', 'green', 'is', 'magenta', 'pentagon', 'rectangle', 'red', 'semicircle', 'square', 'there', 'triangle', 'white', 'yellow', '.'],
    'correct_ratio': 0.5,
    'train_correct_ratio': 0.33,
    'validation_correct_ratio': 0.5,
    'test_correct_ratio': 0.5
}
